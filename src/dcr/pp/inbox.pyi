"""Library Stub."""

import pathlib
from typing import Type

import db.cls_action

def check_and_create_directories() -> None: ...
def create_directory(directory_type: str, directory_name: str) -> None: ...
def initialise_action(
    action_code: str = "",
    directory_name: str = "",
    directory_type: str = "",
    file_name: str = "",
    id_parent: int = 0,
) -> Type[db.cls_action.Action]: ...
def initialise_base(file_path: pathlib.Path) -> None: ...
def prepare_pdf(file: pathlib.Path) -> None: ...
def process_inbox() -> None: ...
def process_inbox_accepted(next_step: str) -> None: ...
def process_inbox_file(file: pathlib.Path) -> None: ...
def process_inbox_rejected(error_code: str, error: str) -> None: ...
