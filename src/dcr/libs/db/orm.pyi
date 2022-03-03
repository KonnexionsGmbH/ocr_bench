"""Library Stub.

Returns:
    [type]: None.
"""
from typing import Callable
from typing import Dict

import libs.cfg
import sqlalchemy.orm

def check_db_up_to_date() -> None: ...
def connect_db() -> None: ...
def create_dbt_document(table_name: str) -> None: ...
def create_dbt_journal(table_name: str) -> None: ...
def create_dbt_run(table_name: str) -> None: ...
def create_dbt_version(
    table_name: str,
) -> None: ...
def create_schema() -> None: ...
def disconnect_db() -> None: ...
def insert_dbt_row(
    table_name: str,
    columns: libs.cfg.Columns,
) -> sqlalchemy.Integer: ...
def insert_journal(
    module_name: str,
    function_name: str,
    document_id: sqlalchemy.Integer,
    journal_action: str,
) -> None: ...
def prepare_connect_db() -> None: ...
def select_document_file_name_sha256(
    document_id: sqlalchemy.Integer, sha256: str
) -> str | None: ...
def select_run_run_id_last() -> int | sqlalchemy.Integer: ...
def select_version_version_unique() -> str: ...
def update_dbt_id(
    table_name: str,
    id_where: sqlalchemy.Integer,
    columns: Dict[str, str],
) -> None: ...
def update_document_status(
    document_columns: libs.cfg.Columns, insert_journal: Callable[[str, str, str], None]
) -> None: ...
def update_version_version(
    version: str,
) -> None: ...
