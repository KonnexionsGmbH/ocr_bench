"""Library Stub."""
from typing import Dict

import libs.cfg
import sqlalchemy.orm

def insert_dbt_row(
    table_name: str,
    columns: libs.cfg.Columns,
) -> sqlalchemy.Integer: ...
def insert_journal_error(
    document_id: sqlalchemy.Integer,
    error: str,
) -> None: ...
def insert_journal_statistics(
    document_id: sqlalchemy.Integer,
) -> None: ...
def select_document_file_name_id(document_id: sqlalchemy.Integer) -> str | None: ...
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
