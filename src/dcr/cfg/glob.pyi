# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
from __future__ import annotations

import os

import dcr.db.cls_action
import dcr.db.cls_db_core
import dcr.db.cls_document
import dcr.db.cls_language
import dcr.db.cls_run
import dcr.db.cls_token
import dcr.db.cls_version

FILE_ENCODING_DEFAULT: str
LOGGER_END: str
LOGGER_START: str

action_curr: dcr.db.cls_action.Action
action_next: dcr.db.cls_action.Action
db_core: dcr.db.cls_db_core.DBCore
directory_inbox: os.PathLike[str] | str
directory_inbox_accepted: os.PathLike[str] | str
directory_inbox_rejected: os.PathLike[str] | str
document: dcr.db.cls_document.Document
language: dcr.db.cls_language.Language
run: dcr.db.cls_run.Run
start_time_document: int
token: dcr.db.cls_token.Token
version: dcr.db.cls_version.Version
