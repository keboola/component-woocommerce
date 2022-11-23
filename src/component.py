"""
Template Component main class.

"""
import datetime
import logging
import os
import sys
from pathlib import Path

import dateparser
from kbc.env_handler import KBCEnvHandler

from result import OrdersWriter, CustomersWriter, ProductsWriter
from woocommerce_cli import WooCommerceClient, error_handling

# configuration variables
STORE_URL = "store_url"
CONSUMER_KEY = "#consumer_key"
CONSUMER_SECRET = "#consumer_secret"
KEY_QUERY_STRING_AUTH = "query_string_auth"
DATE_FROM = "date_from"
DATE_TO = "date_to"
ENDPOINT = "endpoint"
KEY_INCREMENTAL = "load_type"
KEY_ADDITIONAL_OPTIONS = "additional_options"
KEY_FLATTEN_METADATA = "flatten_metadata_values"

KEY_FETCHING_MODE = "fetching_mode"
KEY_CUSTOM_INCREMENTAL_FIELD = "custom_incremental_field"
KEY_CUSTOM_INCREMENTAL_VALUE = "custom_incremental_value"
# #### Keep for debug
KEY_DEBUG = "debug"

# list of mandatory parameters => if some is missing, component will fail with readable message on initialization.
MANDATORY_PARS = [
    STORE_URL,
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ENDPOINT,
]
# MANDATORY_PARS = [KEY_DEBUG]
MANDATORY_IMAGE_PARS = []


class UserException(Exception):
    pass


class Component(KBCEnvHandler):
    def __init__(self, debug=False):
        # for easier local project setup
        default_data_dir = (
            Path(__file__).resolve().parent.parent.joinpath("data").as_posix()
            if not os.environ.get("KBC_DATADIR")
            else None
        )

        KBCEnvHandler.__init__(
            self,
            MANDATORY_PARS,
            log_level=logging.DEBUG if debug else logging.INFO,
            data_path=default_data_dir,
        )
        # override debug from config
        if self.cfg_params.get(KEY_DEBUG):
            debug = True
        if debug:
            logging.getLogger().setLevel(logging.DEBUG)
        else:
            logging.getLogger("woocommerce.component").setLevel(logging.WARNING)
        logging.info("Loading configuration...")

        try:
            # validation of mandatory parameters. Produces ValueError
            self.validate_config(MANDATORY_PARS)
            self.validate_image_parameters(MANDATORY_IMAGE_PARS)
        except ValueError as e:
            logging.exception(e)
            exit(1)

        self.client = WooCommerceClient(
            url=self.cfg_params.get("store_url"),
            consumer_key=self.cfg_params.get(CONSUMER_KEY),
            consumer_secret=self.cfg_params.get(CONSUMER_SECRET),
            version=self.cfg_params.get("version", "wc/v3"),
            query_string_auth=self.cfg_params.get(KEY_QUERY_STRING_AUTH, False)
        )
        self.extraction_time = datetime.datetime.now().isoformat()
        self.flatten_metadata = self.cfg_params.get(KEY_ADDITIONAL_OPTIONS, {}).get(KEY_FLATTEN_METADATA, True)

    def run(self):
        """
        Main execution code
        """
        params = self.cfg_params  # noqa

        last_state = self.get_state_file()
        start_date = end_date = custom_incremental_date = None

        param_start_date = params.get(DATE_FROM, None)
        param_end_date = params.get(DATE_TO, None)
        fetching_mode = params.get(KEY_FETCHING_MODE, "Incremental Fetching with publish date")
        custom_incremental_value = params.get(KEY_CUSTOM_INCREMENTAL_VALUE, None)
        custom_incremental_field = params.get(KEY_CUSTOM_INCREMENTAL_FIELD, None)

        if param_start_date and param_end_date and fetching_mode == "Incremental Fetching with publish date":
            start_date, end_date = self.get_date_period_converted(param_start_date, param_end_date)
            start_date = start_date.replace(microsecond=0).isoformat()
            end_date = end_date.replace(microsecond=0).isoformat()
            logging.info(f"Getting data From: {start_date} To: {end_date}")

        elif custom_incremental_value and custom_incremental_field and \
                fetching_mode == "Incremental Fetching with custom field":
            try:
                custom_incremental_date = dateparser.parse(custom_incremental_value).replace(microsecond=0).isoformat()
            except ValueError as val_err:
                raise UserException("Failed to parse custom incremental date") from val_err
            logging.info(
                f"Getting data From: {custom_incremental_date} Till Now using '{custom_incremental_field}' param")
        else:
            logging.info("Getting all data")
        results = []
        endpoints = params.get("endpoint", ["Orders", "Products", "Customers"])
        for endpoint in endpoints:
            if endpoint.lower() == "orders":
                logging.info("Downloading Orders")
                results.extend(
                    self.download_orders(
                        start_date,
                        end_date,
                        last_state,
                        custom_incremental_field,
                        custom_incremental_date
                    )
                )
            if endpoint.lower() == "products":
                logging.info("Downloading Products")
                results.extend(
                    self.download_products(
                        start_date,
                        end_date,
                        last_state,
                        custom_incremental_field,
                        custom_incremental_date
                    )
                )
            if endpoint.lower() == "customers":
                logging.info("Downloading Customers")
                results.extend(self.download_customers(last_state))

        # get current columns and store in state
        headers = {}
        for r in results:
            file_name = os.path.basename(r.full_path)
            headers[file_name] = r.table_def.columns
        self.write_state_file(headers)

        self.create_manifests(results, incremental=params.get(KEY_INCREMENTAL, True))

    @error_handling
    def download_orders(self, start_date, end_date, file_headers, custom_incremental_field,
                        custom_incremental_date):
        with OrdersWriter(
                self.tables_out_path,
                "order",
                extraction_time=self.extraction_time,
                file_headers=file_headers,
                flatten_metadata=self.flatten_metadata
        ) as writer:
            for data in self.client.get_orders(date_from=start_date, date_to=end_date,
                                               custom_incremental_field=custom_incremental_field,
                                               custom_incremental_date=custom_incremental_date):
                try:
                    for obj in data:
                        writer.write(obj)
                except Exception as err:
                    logging.error(f"Fail to download orders: {err}")
        results = writer.collect_results()
        return results

    @error_handling
    def download_customers(self, file_headers):

        from guppy import hpy  # noqa
        h = hpy()
        with CustomersWriter(
                self.tables_out_path,
                "customer",
                extraction_time=self.extraction_time,
                file_headers=file_headers,
                flatten_metadata=self.flatten_metadata
        ) as writer:
            counter = 0
            for data in self.client.get_customers():
                logging.debug(h.heap())
                logging.debug(f"Processing page {counter}")
                logging.debug(sys.getsizeof(data))
                counter += 1
                try:
                    writer.write_all(data)
                except Exception as err:
                    logging.error(f"Fail to fetch customers {err}")
        results = writer.collect_results()
        return results

    @error_handling
    def download_products(self, start_date, end_date, file_headers, custom_incremental_field,
                          custom_incremental_date):
        with ProductsWriter(
                self.tables_out_path,
                "product",
                prefix="product__",
                extraction_time=self.extraction_time,
                file_headers=file_headers,
                client=self.client,
                flatten_metadata=self.flatten_metadata
        ) as writer:
            for data in self.client.get_products(
                    date_from=start_date, date_to=end_date, custom_incremental_field=custom_incremental_field,
                    custom_incremental_date=custom_incremental_date
            ):
                try:
                    for product in data:
                        writer.write(product)
                except Exception as err:
                    logging.error(f"Fail to fetch  products {err}")
        results = writer.collect_results()
        return results


"""
        Main entrypoint
"""
if __name__ == "__main__":
    if len(sys.argv) > 1:
        debug_arg = sys.argv[1]
    else:
        debug_arg = False
    try:
        comp = Component(debug_arg)
        comp.run()
    except Exception as exc:
        logging.exception(exc)
        exit(1)
