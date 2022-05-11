"""Library Stub."""
import db.utils
import sqlalchemy.engine

def delete_dbt_id(
    table_name: str,
    id_where: int | sqlalchemy.Integer,
) -> None: ...
def dml_prepare(dbt_name: str) -> sqlalchemy.Table: ...
def insert_dbt_row(
    table_name: str,
    columns: db.utils.Columns,
) -> sqlalchemy.Integer: ...
def insert_document_child() -> None: ...
def select_content_tetml(
    conn: sqlalchemy.engine.Connection, dbt: sqlalchemy.Table, document_id: sqlalchemy.Integer
) -> sqlalchemy.engine.CursorResult: ...
def select_document(
    conn: sqlalchemy.engine.Connection, dbt: sqlalchemy.Table, next_step: str
) -> sqlalchemy.engine.CursorResult: ...
def select_document_base_file_name() -> str | None: ...
def select_document_file_name_id(document_id: sqlalchemy.Integer) -> str | None: ...
def select_document_file_name_sha256(document_id: sqlalchemy.Integer, sha256: str) -> str | None: ...
def select_language(conn: sqlalchemy.engine.Connection, dbt: sqlalchemy.Table) -> sqlalchemy.engine.CursorResult: ...
def select_run_id_run_last() -> int | sqlalchemy.Integer: ...
def select_version_version_unique() -> str: ...
def update_dbt_id(
    table_name: str,
    id_where: int | sqlalchemy.Integer,
    columns: db.utils.Columns,
) -> None: ...
def update_document_error(document_id: sqlalchemy.Integer, error_code: str, error_msg: str) -> None: ...
def update_document_statistics(
    document_id: sqlalchemy.Integer,
    status: str,
) -> int: ...
