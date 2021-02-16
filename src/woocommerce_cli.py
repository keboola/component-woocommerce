import datetime
import logging

from woocommerce import API


RESULTS_PER_PAGE = 100


# 401, 500
class UnauthorizedError(Exception):
    pass


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
            if response.status_code == 401:
                logging.error(f"{response.json()}")
                raise UnauthorizedError(response.text)

    def _fetch_data(self, endpoint, params):
        """
        Fetch all data
        """
        page_count = 1
        response = self.session.get(endpoint, params=params)
        if response.status_code == 200:
            yield response.json()
            total_pages = int(response.headers.get("X-WP-TotalPages", 1))
            while page_count < total_pages:
                page_count += 1
                params["page"] = page_count
                response = self.session.get(endpoint, params=params)
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
