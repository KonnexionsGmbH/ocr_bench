"""Library Stub."""
from typing import List

def check_db_up_to_date() -> None: ...
def get_args(argv: List[str]) -> dict[str, bool]: ...
def initialise_logger() -> None: ...
def load_data_from_dbt_language() -> None: ...
def main(argv: List[str]) -> None: ...
def process_convert_image_2_pdf() -> None: ...
def process_convert_non_pdf_2_pdf() -> None: ...
def process_convert_pdf_2_image() -> None: ...
def process_documents(args: dict[str, bool]) -> None: ...
def process_extract_text_from_pdf() -> None: ...
def process_inbox_directory() -> None: ...
def process_store_from_parser() -> None: ...
def process_tokenize() -> None: ...
