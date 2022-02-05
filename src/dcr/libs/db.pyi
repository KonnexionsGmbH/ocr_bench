# pylint: disable=unused-argument
"""Library stub."""

import logging
import sqlite3
from typing import Dict

import sqlalchemy.orm
from libs import cfg

def check_db_up_to_date(logger: logging.Logger) -> None: ...
def connect_db(logger: logging.Logger) -> None: ...
def connect_db_core(logger: logging.Logger) -> None: ...
def create_dbt_document() -> None: ...
def create_dbt_journal() -> None: ...
def create_dbt_run() -> None: ...
def create_dbt_run_row(logger: logging.Logger) -> None: ...
def create_dbt_version() -> sqlalchemy.Table: ...
def create_db_trigger_modified_at(
    logger: logging.Logger, conn: sqlite3.Connection, table_name: str
) -> None: ...
def create_db_triggers_modified_at(logger: logging.Logger) -> None: ...
def disconnect_db(logger: logging.Logger) -> None: ...
def insert_dbt_row(
    logger: logging.Logger, table: str, columns: cfg.Columns
) -> None: ...
def select_dbt_id_last(
    logger: logging.Logger, table_name: str
) -> sqlalchemy.Integer: ...
def select_version_version_unique(logger: logging.Logger) -> str: ...
def update_dbt_id(
    logger: logging.Logger,
    table_name: str,
    id_where: sqlalchemy.Integer,
    columns: Dict[str, str],
) -> None: ...
def upgrade_db(logger: logging.Logger) -> None: ...
