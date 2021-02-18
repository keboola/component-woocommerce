from typing import List
from kbc.result import ResultWriter, KBCTableDef

EXTRACTION_TIME = "extraction_time"
KEY_ROW_NR = "row_nr"  # take row number


class MetadataWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: List[str] = None,
        prefix="",
        file_headers=None,
    ) -> None:
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        result_name = f"{prefix}metadata"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=result_name,
                pk=pk,
                columns=file_headers.get(f"{prefix}metadata.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extration_time = extraction_time
        self.result_dir_path = result_dir_path


class FeeLinesWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: List[str] = None,
        prefix="",
        file_headers=None,
    ) -> None:
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        result_name = f"{prefix}fee_lines"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=result_name,
                pk=pk,
                columns=file_headers.get(f"{prefix}fee_lines.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extration_time = extraction_time
        self.result_dir_path = result_dir_path


class RefundsWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: List[str] = None,
        prefix="",
        file_headers=None,
    ) -> None:
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        result_name = f"{prefix}refunds"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=result_name,
                pk=pk,
                columns=file_headers.get(f"{prefix}refunds.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extration_time = extraction_time
        self.result_dir_path = result_dir_path


class LineItemsWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: List[str] = None,
        prefix: str = "",
        file_headers=None,
    ):
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        file_name = f"{prefix}line_items"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=file_name,
                pk=pk,
                columns=file_headers.get(f"{file_name}.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extraction_time = extraction_time
        self.result_dir_path = result_dir_path
        primary_keys = pk + ["line_item_id"]
        # taxes writer
        self.taxes_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}line_items__taxes",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}line_items__taxes.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )
        # meta_data writer
        self.meta_data_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}line_items__meta_data",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}line_items__meta_data.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        # flatten obj
        line_item_id = data["id"]
        taxes = data.pop("taxes", [])
        meta_data = data.pop("meta_data", [])
        self.taxes_writer.write_all(
            taxes,
            user_values={
                **user_values,
                "line_item_id": line_item_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.meta_data_writer.write_all(
            meta_data,
            user_values={
                **user_values,
                "line_item_id": line_item_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )

        super().write(data, file_name, user_values, object_from_arrays, write_header)

    def collect_results(self):
        results = []
        results.extend(self.taxes_writer.collect_results())
        results.extend(self.meta_data_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.taxes_writer.close()
        self.meta_data_writer.close()
        super().close()


class TaxLinesWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: list = None,
        prefix="",
        file_headers=None,
    ) -> None:
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        file_name = f"{prefix}tax_lines"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=file_name,
                pk=pk,
                columns=file_headers.get(f"{file_name}.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extraction_time = extraction_time
        self.result_dir_path = result_dir_path
        primary_keys = pk + ["tax_lines_id"]
        # meta_data writer
        self.meta_data_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}tax_lines__meta_data",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}tax_lines__meta_data.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        # flatten obj
        tax_lines_id = data["id"]
        meta_data = data.pop("meta_data", [])
        self.meta_data_writer.write_all(
            meta_data,
            user_values={
                **user_values,
                "tax_lines_id": tax_lines_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )

        super().write(data, file_name, user_values, object_from_arrays, write_header)

    def collect_results(self):
        results = []
        results.extend(self.meta_data_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.meta_data_writer.close()
        super().close()


class ShippingLinesWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: list = None,
        prefix="",
        file_headers=None,
    ) -> None:
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        file_name = f"{prefix}shipping_lines"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=file_name,
                pk=pk,
                columns=file_headers.get(f"{file_name}.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extraction_time = extraction_time

        self.result_dir_path = result_dir_path

        # tax_lines writer
        primary_keys = pk + ["shipping_lines_id"]
        self.taxes_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}shipping_lines__taxes",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}shipping_lines__taxes.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

        # meta_data writer
        self.meta_data_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}shipping_lines__meta_data",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}shipping_lines__meta_data.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        # flatten obj
        shipping_line_id = data["id"]
        taxes = data.pop("taxes", [])
        meta_data = data.pop("meta_data", [])

        self.taxes_writer.write_all(
            taxes,
            user_values={
                **user_values,
                "shipping_lines_id": shipping_line_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.meta_data_writer.write_all(
            meta_data,
            user_values={
                **user_values,
                "shipping_lines_id": shipping_line_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        super().write(data, file_name, user_values, object_from_arrays, write_header)

    def collect_results(self):
        results = []
        results.extend(self.taxes_writer.collect_results())
        results.extend(self.meta_data_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.taxes_writer.close()
        self.meta_data_writer.close()
        super().close()


class CouponLinesWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path,
        extraction_time,
        additional_pk: list = None,
        prefix="",
        file_headers=None,
    ):
        pk = ["id"]
        if additional_pk:
            pk.extend(additional_pk)
        file_name = f"{prefix}coupon_lines"
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=file_name,
                pk=pk,
                columns=file_headers.get(f"{file_name}.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extraction_time = extraction_time

        self.result_dir_path = result_dir_path
        primary_keys = pk + ["coupon_lines_id"]
        self.meta_data_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}coupon_lines__meta_data",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}coupon_lines__meta_data.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        # flatten obj
        coupon_lines_id = data["id"]
        meta_data = data.pop("meta_data", [])
        self.meta_data_writer.write_all(
            meta_data,
            user_values={
                **user_values,
                "coupon_lines_id": coupon_lines_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )

        super().write(data, file_name, user_values, object_from_arrays, write_header)

    def collect_results(self):
        results = []
        results.extend(self.meta_data_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.meta_data_writer.close()
        super().close()


class OrdersWriter(ResultWriter):
    def __init__(
        self, result_dir_path, result_name, extraction_time, file_headers=None
    ):
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=result_name,
                pk=["id"],
                columns=file_headers.get("order.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extraction_time = extraction_time
        self.user_value_cols = ["extraction_time"]
        self.result_dir_path = result_dir_path

        self.line_items_writer = LineItemsWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )

        self.tax_lines_writer = TaxLinesWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )

        self.shipping_lines_writer = ShippingLinesWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )
        self.order_meta_data_writer = MetadataWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )
        self.coupon_lines_writer = CouponLinesWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )
        self.fee_lines_writer = FeeLinesWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )
        self.refunds_writer = RefundsWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["order_id"],
            file_headers=file_headers,
            prefix="order__",
        )

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        excludes = ["_links", "customer_user_agent"]
        for field in excludes:
            data.pop(field)
        order_id = data["id"]
        line_items = data.pop("line_items", [])
        tax_lines = data.pop("self.tax_lines_writer", [])
        shipping_lines = data.pop("shipping_lines", [])
        order_meta_data = data.pop("meta_data", [])
        coupon_lines = data.pop("coupon_lines", [])
        refunds = data.pop("fee_lines", [])
        fee_lines = data.pop("fee_lines", [])
        self.line_items_writer.write_all(
            line_items,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        self.tax_lines_writer.write_all(
            tax_lines,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        self.shipping_lines_writer.write_all(
            shipping_lines,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        self.order_meta_data_writer.write_all(
            order_meta_data,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        self.coupon_lines_writer.write_all(
            coupon_lines,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        self.fee_lines_writer.write_all(
            fee_lines,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        self.refunds_writer.write_all(
            refunds,
            user_values={"order_id": order_id, EXTRACTION_TIME: self.extraction_time},
        )
        super().write(
            data=data,
            file_name=file_name,
            user_values=user_values,
            object_from_arrays=object_from_arrays,
            write_header=write_header,
        )

    def collect_results(self):
        results = []
        results.extend(self.line_items_writer.collect_results())
        results.extend(self.tax_lines_writer.collect_results())
        results.extend(self.shipping_lines_writer.collect_results())
        results.extend(self.order_meta_data_writer.collect_results())
        results.extend(self.coupon_lines_writer.collect_results())
        results.extend(self.fee_lines_writer.collect_results())
        results.extend(self.refunds_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.line_items_writer.close()
        self.tax_lines_writer.close()
        self.shipping_lines_writer.close()
        self.order_meta_data_writer.close()
        self.coupon_lines_writer.close()
        self.fee_lines_writer.close()
        self.refunds_writer.close()
        super().close()


class CustomersWriter(ResultWriter):
    def __init__(
        self, result_dir_path, result_name, extraction_time, file_headers=None
    ):
        super().__init__(
            result_dir_path,
            KBCTableDef(
                name=result_name,
                pk=["id"],
                columns=file_headers.get("customer.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.meta_data_writer = MetadataWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["customer_id"],
            file_headers=file_headers,
            prefix="customer__",
        )
        self.extraction_time = extraction_time
        self.user_value_cols = ["extraction_time"]
        self.result_dir_path = result_dir_path

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        excludes = ["_links"]
        for field in excludes:
            data.pop(field)
        customer_id = data.get("id")
        meta_data = data.pop("meta_data", [])
        self.meta_data_writer.write_all(
            meta_data,
            user_values={
                "customer_id": customer_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        super().write(
            data,
            file_name=file_name,
            user_values=user_values,
            object_from_arrays=object_from_arrays,
            write_header=write_header,
        )

    def collect_results(self):
        results = []
        results.extend(self.meta_data_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.meta_data_writer.close()
        super().close()


class ProductsWriter(ResultWriter):
    def __init__(
        self,
        result_dir_path: str,
        result_name: str,
        extraction_time,
        prefix="",
        file_headers=None,
        client=None,
    ):
        self.client = client
        pk = ["id"]
        super().__init__(
            result_dir_path,
            table_def=KBCTableDef(
                name=result_name,
                pk=pk,
                columns=file_headers.get("product.csv", []),
                destination="",
            ),
            fix_headers=True,
            flatten_objects=True,
            child_separator="__",
        )
        self.extraction_time = extraction_time
        self.user_value_cols = ["extraction_time"]
        self.result_dir_path = result_dir_path
        primary_keys = pk + ["product_id"]
        self.categories_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}categories",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}categories.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

        self.images_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}images",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}images.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

        self.attributes_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}attributes",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}attributes.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

        self.default_attributes_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}default_attributes",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}default_attributes.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )

        self.tags_writer = ResultWriter(
            result_dir_path,
            KBCTableDef(
                name=f"{prefix}tags",
                pk=primary_keys,
                columns=file_headers.get(f"{prefix}tags.csv", []),
                destination="",
            ),
            flatten_objects=True,
            fix_headers=True,
            child_separator="__",
        )
        self.meta_data_writer = MetadataWriter(
            result_dir_path,
            extraction_time,
            additional_pk=["product_id"],
            file_headers=file_headers,
            prefix="product__",
        )

    def write(
        self,
        data,
        file_name=None,
        user_values=None,
        object_from_arrays=False,
        write_header=True,
    ):
        product_id = data.get("id", "Not found")
        excludes = ["_links", "downloads"]
        for field in excludes:
            data.pop(field)
        categories = data.pop("categories", [])
        images = data.pop("images", [])
        attributes = data.pop("attributes", [])
        default_attributes = data.pop("default_attributes", [])
        meta_data = data.pop("meta_data", [])
        tags = data.pop("tags", [])
        self.categories_writer.write_all(
            categories,
            user_values={
                "product_id": product_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.images_writer.write_all(
            images,
            user_values={
                "product_id": product_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.attributes_writer.write_all(
            attributes,
            user_values={
                "product_id": product_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.default_attributes_writer.write_all(
            default_attributes,
            user_values={
                "product_id": product_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.tags_writer.write_all(
            tags,
            user_values={
                "product_id": product_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        self.meta_data_writer.write_all(
            meta_data,
            user_values={
                "product_id": product_id,
                EXTRACTION_TIME: self.extraction_time,
            },
        )
        super().write(data, file_name, user_values, object_from_arrays, write_header)

    def collect_results(self):
        results = []
        results.extend(self.categories_writer.collect_results())
        results.extend(self.images_writer.collect_results())
        results.extend(self.attributes_writer.collect_results())
        results.extend(self.default_attributes_writer.collect_results())
        results.extend(self.tags_writer.collect_results())
        results.extend(self.meta_data_writer.collect_results())
        results.extend(super().collect_results())
        return results

    def close(self):
        self.categories_writer.close()
        self.images_writer.close()
        self.attributes_writer.close()
        self.default_attributes_writer.close()
        self.tags_writer.close()
        self.meta_data_writer.close()
        super().close()
