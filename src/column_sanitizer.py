import csv
import hashlib
import os
from typing import Dict, List


MAX_COLUMN_LENGTH = 64
PREFIX_LENGTH = 36
HASH_LENGTH = 8
SUFFIX_LENGTH = 16


def sanitize_column_name(name: str) -> str:
    if len(name) <= MAX_COLUMN_LENGTH:
        return name
    name_hash = hashlib.md5(name.encode()).hexdigest()[:HASH_LENGTH]
    prefix = name[:PREFIX_LENGTH]
    suffix = name[-SUFFIX_LENGTH:]
    return f"{prefix}__{name_hash}__{suffix}"


def sanitize_csv_columns(
    input_path: str,
    output_path: str,
) -> Dict[str, str]:
    column_mapping: Dict[str, str] = {}
    with open(input_path, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        new_headers: List[str] = []
        for header in headers:
            new_header = sanitize_column_name(header)
            if new_header != header:
                column_mapping[header] = new_header
            new_headers.append(new_header)
        with open(output_path, "w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(new_headers)
            for row in reader:
                writer.writerow(row)
    return column_mapping


def write_column_mapping(
    mapping: Dict[str, str],
    output_path: str,
) -> None:
    if not mapping:
        return
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["original_column", "sanitized_column"])
        for original, sanitized in mapping.items():
            writer.writerow([original, sanitized])


def process_output_files(output_dir: str) -> None:
    tables_dir = os.path.join(output_dir, "tables")
    if not os.path.exists(tables_dir):
        return
    for filename in os.listdir(tables_dir):
        if not filename.endswith(".csv"):
            continue
        if filename.endswith("__column-mapping.csv"):
            continue
        filepath = os.path.join(tables_dir, filename)
        temp_path = filepath + ".tmp"
        column_mapping = sanitize_csv_columns(filepath, temp_path)
        os.replace(temp_path, filepath)
        if column_mapping:
            base_name = filename[:-4]
            mapping_filename = f"{base_name}__column-mapping.csv"
            mapping_path = os.path.join(tables_dir, mapping_filename)
            write_column_mapping(column_mapping, mapping_path)
