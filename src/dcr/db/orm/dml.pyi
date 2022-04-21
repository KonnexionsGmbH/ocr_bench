"""Library Stub."""
import pathlib
from typing import Dict

import libs.cfg
import sqlalchemy.orm
from sqlalchemy import Table
from sqlalchemy import engine
from sqlalchemy.engine import Connection

def get_pdf_pages_no(
    file_path: pathlib.Path,
    file_type: str,
) -> sqlalchemy.Integer | None: ...
def insert_dbt_row(
    table_name: str,
    columns: libs.cfg.Columns,
) -> sqlalchemy.Integer: ...
def insert_document_base() -> None: ...
def insert_document_child() -> None: ...
def dml_prepare(dbt_name: str) -> Table: ...
def select_content_tetml_page(
    conn: Connection, dbt: Table, document_id: sqlalchemy.Integer
) -> engine.CursorResult: ...
def select_document(conn: Connection, dbt: Table, next_step: str) -> engine.CursorResult: ...
def select_document_base_file_name() -> str | None: ...
def select_document_file_name_id(document_id: sqlalchemy.Integer) -> str | None: ...
def select_document_file_name_sha256(
    document_id: sqlalchemy.Integer, sha256: str
) -> str | None: ...
def select_language(conn: Connection, dbt: Table) -> engine.CursorResult: ...
def select_run_run_id_last() -> int | sqlalchemy.Integer: ...
def select_version_version_unique() -> str: ...
def update_dbt_id(
    table_name: str,
    id_where: sqlalchemy.Integer,
    columns: Dict[str, str],
) -> None: ...
def update_document_error(
    document_id: sqlalchemy.Integer, error_code: str, error_msg: str
) -> None: ...
def update_document_statistics(
    document_id: sqlalchemy.Integer,
    status: str,
) -> None: ...
