"""
Template Component main class.

"""
import datetime
import logging
import os
import sys
from pathlib import Path

from kbc.env_handler import KBCEnvHandler

from woocommerce_cli import WooCommerceClient
from result import OrdersWriter, CustomersWriter, ProductsWriter

# configuration variables
STORE_URL = "store_url"
CONSUMER_KEY = "consumer_key"
CONSUMER_SECRET = "consumer_secret"
DATE_FROM = "date_from"
DATE_TO = "date_to"
# #### Keep for debug
KEY_DEBUG = "debug"

# list of mandatory parameters => if some is missing, component will fail with readable message on initialization.
MANDATORY_PARS = [STORE_URL, CONSUMER_KEY, CONSUMER_SECRET, DATE_FROM, DATE_TO]
# MANDATORY_PARS = [KEY_DEBUG]
MANDATORY_IMAGE_PARS = []

APP_VERSION = "0.0.1"


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
        logging.info("Running version %s", APP_VERSION)
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
            consumer_key=self.cfg_params.get("consumer_key"),
            consumer_secret=self.cfg_params.get("consumer_secret"),
            version=self.cfg_params.get("version", "wc/v3"),
        )
        self.extraction_time = datetime.datetime.now().isoformat()

    def run(self):
        """
        Main execution code
        """
        params = self.cfg_params  # noqa

        last_state = self.get_state_file()
        start_date, end_date = self.get_date_period_converted(
            params[DATE_FROM], params[DATE_TO]
        )
        # start_date, end_date = self.get_date_period_converted('2 month ago', 'now')
        results = []
        sliced_results = []
        logging.info(f"Getting data {start_date}")
        if params["endpoint"] == "orders":
            results.extend(
                self.download_orders(
                    start_date.replace(microsecond=0).isoformat(),
                    end_date.replace(microsecond=0).isoformat(),
                    last_state,
                )
            )
        elif params["endpoint"] == "products":
            results.extend(
                self.download_products(
                    start_date.replace(microsecond=0).isoformat(),
                    end_date.replace(microsecond=0).isoformat(),
                    last_state,
                )
            )
        elif params["endpoint"] == "customers":
            results.extend(self.download_customers(last_state))
        else:  # Fetch all
            results.extend(
                self.download_orders(
                    start_date.replace(microsecond=0).isoformat(),
                    end_date.replace(microsecond=0).isoformat(),
                    last_state,
                )
            )
            results.extend(
                self.download_products(
                    start_date.replace(microsecond=0).isoformat(),
                    end_date.replace(microsecond=0).isoformat(),
                    last_state,
                )
            )
            results.extend(self.download_customers(last_state))

        # get current columns and store in state
        headers = {}
        for r in results:
            file_name = os.path.basename(r.full_path)
            headers[file_name] = r.table_def.columns
        self.write_state_file(headers)

        # separate sliced results
        sliced_results.extend(
            [
                results.pop(idx)
                for idx, r in enumerate(results)
                if os.path.isdir(r.full_path)
            ]
        )

        self.create_manifests(results, incremental=True)
        self.create_manifests(sliced_results, headless=True, incremental=True)

    def download_orders(self, start_date, end_date, file_headers):
        with OrdersWriter(
            self.tables_out_path,
            "order",
            extraction_time=self.extraction_time,
            file_headers=file_headers,
        ) as writer:
            for obj in self.client.get_orders(date_from=start_date, date_to=end_date):
                try:
                    writer.write(obj)
                except Exception as err:
                    logging.error(f"in download orders: {err}")
        results = writer.collect_results()
        return results

    def download_customers(self, file_headers):
        with CustomersWriter(
            self.tables_out_path,
            "customer",
            extraction_time=self.extraction_time,
            file_headers=file_headers,
        ) as writer:
            for customer in self.client.get_customers():
                try:
                    writer.write(customer)
                except Exception as err:
                    logging.error(f"Fail to fetch customers {err}")
        results = writer.collect_results()
        return results

    def download_products(self, start_date, end_date, file_headers):
        with ProductsWriter(
            self.tables_out_path,
            "products",
            prefix="products_",
            extraction_time=self.extraction_time,
            file_headers=file_headers,
            client=self.client,
        ) as writer:
            for product in self.client.get_products(
                date_from=start_date, date_to=end_date
            ):
                try:
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
