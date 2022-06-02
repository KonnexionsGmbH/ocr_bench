"""Module cfg.glob: DCR Global Data."""
from __future__ import annotations

import logging
import os

import cfg.cls_setup
import db.cls_action
import db.cls_db_core
import db.cls_document
import db.cls_language
import db.cls_run
import nlp.cls_line_type
import nlp.cls_text_parser
import nlp.cls_tokenizer_spacy

# -----------------------------------------------------------------------------
# Global Constants.
# -----------------------------------------------------------------------------
FILE_ENCODING_DEFAULT: str = "utf-8"

INFORMATION_NOT_YET_AVAILABLE: str = "n/a"

LOGGER_END: str = "End"
LOGGER_FATAL_HEAD: str = "FATAL ERROR: program abort =====> "
LOGGER_FATAL_TAIL: str = " <===== FATAL ERROR"
LOGGER_PROGRESS_UPDATE: str = "Progress update "
LOGGER_START: str = "Start"

# -----------------------------------------------------------------------------
# Global Variables.
# -----------------------------------------------------------------------------
action_curr: type[db.cls_action.Action]
action_next: type[db.cls_action.Action]

db_core: type[db.cls_db_core.DBCore]

directory_inbox: os.PathLike[str] | str
directory_inbox_accepted: os.PathLike[str] | str
directory_inbox_rejected: os.PathLike[str] | str

document: type[db.cls_document.Document]

language: type[db.cls_language.Language]

line_type: type[nlp.cls_line_type.LineType]

logger: logging.Logger

run: type[db.cls_run.Run]

setup: type[cfg.cls_setup.Setup]

start_time_document: int

text_parser: type[nlp.cls_text_parser.TextParser]

tokenizer_spacy: type[nlp.cls_tokenizer_spacy.TokenizerSpacy]
