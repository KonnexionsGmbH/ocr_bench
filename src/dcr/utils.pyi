# Copyright (c) 2022 Konnexions GmbH. All rights reserved. Use of this
# source code is governed by the Konnexions Public License (KX-PL)
# Version 2020.05, that can be found in the LICENSE file.

"""Module stub file."""
import pathlib

def check_exists_object(
    is_action_curr: bool = False,
    is_action_next: bool = False,
    is_db_core: bool = False,
    is_document: bool = False,
    is_run: bool = False,
) -> None: ...
def compute_sha256(file: pathlib.Path) -> str: ...
def delete_auxiliary_file(full_name: pathlib.Path | str) -> None: ...
def get_file_type(file_name: pathlib.Path | str | None) -> str: ...
def get_path_name(name: pathlib.Path | str | None) -> pathlib.Path | str: ...
def get_pdf_pages_no(
    file_name: pathlib.Path | str,
) -> int: ...
def progress_msg(msg: str) -> None: ...
def progress_msg_connected(database: str | None, user: str | None) -> None: ...
def progress_msg_core(msg: str) -> None: ...
def progress_msg_disconnected() -> None: ...
def progress_msg_empty_before(msg: str) -> None: ...
def progress_msg_line_type_heading(msg: str) -> None: ...
def progress_msg_line_type_list_bullet(msg: str) -> None: ...
def progress_msg_line_type_list_number(msg: str) -> None: ...
def reset_statistics_total() -> None: ...
def show_statistics_language() -> None: ...
def show_statistics_total() -> None: ...
def terminate_fatal(error_msg: str) -> None: ...
def terminate_fatal_setup(error_msg: str) -> None: ...
