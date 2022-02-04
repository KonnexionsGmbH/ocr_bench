# pylint: disable=unused-argument
"""Library stub."""

import logging
import sqlite3
from typing import Dict
from typing import List

import sqlalchemy.orm
from libs import cfg

def check_db_up_to_date(logger: logging.Logger) -> None: ...
def connect_database(logger: logging.Logger) -> None: ...
def create_database(logger: logging.Logger) -> None: ...
def create_or_upgrade_database(logger: logging.Logger) -> None: ...
def create_table_document() -> None: ...
def create_table_journal() -> None: ...
def create_table_run() -> None: ...
def create_table_run_entry(logger: logging.Logger) -> None: ...
def create_table_version() -> sqlalchemy.Table: ...
def create_trigger_dbc_modified_at(
    logger: logging.Logger, conn: sqlite3.Connection, table_name: str
) -> None: ...
def create_triggers_dbc_modified_at(
    logger: logging.Logger, table_names: List[str]
) -> None: ...
def disconnect_database(logger: logging.Logger) -> None: ...
def insert_table(
    logger: logging.Logger, table: str, columns: cfg.Columns
) -> None: ...
def select_table_id_last(
    logger: logging.Logger, table_name: str
) -> sqlalchemy.Integer: ...
def select_version_version_unique(logger: logging.Logger) -> str: ...
def update_table_id(
    logger: logging.Logger,
    table_name: str,
    id_where: sqlalchemy.Integer,
    columns: Dict[str, str],
) -> None: ...
def upgrade_database(logger: logging.Logger) -> None: ...
