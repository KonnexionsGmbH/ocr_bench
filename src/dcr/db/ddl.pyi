"""Library Stub."""
import pathlib
from typing import List

def create_db_trigger_function(column_name: str) -> None: ...
def create_db_trigger_created_at(table_name: str) -> None: ...
def create_db_trigger_modified_at(table_name: str) -> None: ...
def create_db_triggers(table_names: List[str]) -> None: ...
def create_dbt_content_tetml_line(table_name: str) -> None: ...
def create_dbt_content_tetml_word(table_name: str) -> None: ...
def create_dbt_content_token(table_name: str) -> None: ...
def create_dbt_document(table_name: str) -> None: ...
def create_dbt_language(table_name: str) -> None: ...
def create_dbt_run(table_name: str) -> None: ...
def create_dbt_version(
    table_name: str,
) -> None: ...
def create_schema() -> None: ...
def load_db_data_from_json(initial_database_data: pathlib.Path) -> None: ...
