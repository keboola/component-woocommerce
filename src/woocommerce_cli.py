import datetime
import functools
import logging
import math
import sys

import backoff
import requests
from requests import Response
from woocommerce import API

RESULTS_PER_PAGE = 100

# We will retry a 500 error a maximum of 5 times before giving up
MAX_RETRIES = 5


class ConnectionError(Exception):
    pass


class WooCommerceClientError(Exception):
    pass


class HTTPSProtocolError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


def is_not_status_code_fn(status_code):
    def gen_fn(exc):
        if getattr(exc, "code", None) and exc.code not in status_code:
            return True
        # Retry other errors up to the max
        return False

    return gen_fn


def leaky_bucket_handler(details):
    logging.info("Received 429 -- sleeping for %s seconds", details["wait"])


def retry_handler(details):
    logging.info(
        "Received 500 or retryable error -- Retry %s/%s", details["tries"], MAX_RETRIES
    )


# pylint: disable=unused-argument
def retry_after_wait_gen(**kwargs):
    # This is called in an except block so we can retrieve the exception
    # and check it.
    exc_info = sys.exc_info()
    resp = exc_info[1].response
    # Retry-After is an undocumented header. But honoring
    # it was proven to work in our spikes.
    # It's been observed to come through as lowercase, so fallback if not present
    sleep_time_str = resp.headers.get("Retry-After", resp.headers.get("retry-after"))
    yield math.floor(float(sleep_time_str) * 2)


def error_handling(fnc):
    @backoff.on_exception(
        backoff.expo,
        (
                requests.exceptions.HTTPError,
                requests.exceptions.Timeout,
                requests.exceptions.ConnectionError,
        ),
        giveup=is_not_status_code_fn(range(500, 599)),
        on_backoff=retry_handler,
        max_tries=MAX_RETRIES,
    )
    @backoff.on_exception(
        retry_after_wait_gen,
        requests.exceptions.ConnectionError,
        giveup=is_not_status_code_fn([429]),
        on_backoff=leaky_bucket_handler,
        # No jitter as we want a constant value
        jitter=None,
    )
    @functools.wraps(fnc)
    def wrapper(*args, **kwargs):
        return fnc(*args, **kwargs)

    return wrapper


def response_error_handling(func):
    """Function, that handles response handling of HTTP requests."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            logging.error(e, exc_info=True)
            # Handle different error codes
            raise WooCommerceClientError(
                "The resource was not found. Please check your store url!"
            ) from e
        except Exception as e:
            raise e

    return wrapper


class WooCommerceClient:
    def __init__(
            self,
            url: str,
            consumer_key: str,
            consumer_secret: str,
            version: str = "wc/v3",
            authenticate: bool = True,
    ):
        self.session = API(
            url=url,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            version=version,
        )
        if authenticate:
            response = self.session.get("")
            self._handle_response(response)

    def _handle_response(self, response: Response):
        try:
            if response.status_code == 401:
                r = response.json()
                msg = f"message: {r['message']} error: {r['code']} status: {r['data']['status']}"
                logging.error(msg)
                raise UnauthorizedError(msg)
            response.raise_for_status()
        except requests.exceptions.SSLError as err:
            logging.error(err)
            raise HTTPSProtocolError(
                "Verify the site has valid ssl certificates"
            ) from err
        except requests.exceptions.ConnectionError as err:
            logging.error(err)
            raise ConnectionError(
                "Failed to establish a connection, please correct and verify the store_url"
            ) from err

    @error_handling
    def _fetch_data(self, endpoint, params):
        """
        Fetch all data
        """
        page_count = 1
        # if any date_from or date_to is None then download all data for orders and products
        if endpoint in ["orders", "products"] and not (
                params.get("after") or params.get("before")
        ):
            params.pop("after")
            params.pop("before")
        response = self.session.get(endpoint, params=params)
        self._handle_response(response)
        if response.status_code == 200:
            yield response.json()
            total_pages = int(response.headers.get("X-WP-TotalPages", 1))
            while page_count < total_pages:
                page_count += 1
                params["page"] = page_count
                response = self.session.get(endpoint, params=params)
                response.raise_for_status()
                if response.status_code == 200:
                    yield response.json()

    def get_orders(
            self,
            date_from: str = "",
            date_to: str = datetime.datetime.utcnow().replace(microsecond=0).isoformat(),
            status: str = "any",
            per_page: int = RESULTS_PER_PAGE,
    ):
        """
        Get all orders

        after: str: date_from
        before: str: date_to
        """
        params = {
            "per_page": per_page,
            "status": status,
            "after": date_from,
            "before": date_to,
        }
        data = self._fetch_data("orders", params)
        return data

    def get_products(
            self,
            date_from: str = "",
            date_to: str = datetime.datetime.utcnow().replace(microsecond=0).isoformat(),
            status: str = "any",
            per_page: int = RESULTS_PER_PAGE,
    ):
        """
        Get all products
        """
        params = {
            "per_page": per_page,
            "status": status,
            "after": date_from,
            "before": date_to,
        }
        data = self._fetch_data("products", params)
        return data

    def get_customers(self, per_page: int = RESULTS_PER_PAGE):
        """
        Get all customers
        """
        params = {"per_page": per_page}
        data = self._fetch_data("customers", params)
        return data
