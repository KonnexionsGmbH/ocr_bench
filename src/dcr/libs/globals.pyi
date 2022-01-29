"""Library stub."""
from os import PathLike
from typing import Dict

ACTION_ALL_COMPLETE: str
ACTION_DB_CREATE_OR_UPGRADE: str
ACTION_PROCESS_INBOX: str
ACTION_PROCESS_INBOX_OCR: str

CONFIG: Dict[str, PathLike[str] | str]

DCR_CFG_DATABASE_FILE: str
DCR_CFG_DATABASE_URL: str
DCR_CFG_DCR_VERSION: str
DCR_CFG_DIRECTORY_INBOX: str
DCR_CFG_DIRECTORY_INBOX_ACCEPTED: str
DCR_CFG_DIRECTORY_INBOX_OCR: str
DCR_CFG_DIRECTORY_INBOX_OCR_ACCEPTED: str
DCR_CFG_DIRECTORY_INBOX_OCR_REJECTED: str
DCR_CFG_DIRECTORY_INBOX_REJECTED: str
DCR_CFG_FILE: str
DCR_CFG_SECTION: str

FILE_ENCODING_DEFAULT: str
FILE_EXTENSION_PDF: str

LOCALE: str

LOGGER_CFG_FILE: str
LOGGER_END: str
LOGGER_FATAL_HEAD: str
LOGGER_FATAL_TAIL: str
LOGGER_PROGRESS_UPDATE: str
LOGGER_START: str
