# src/yatl/utils.py

import os
from typing import Any, Dict, Optional

from .compiler import YATLCompiler
from .parser import YATLParser
from .runtime import YATLRuntime
from .validator import YATLValidator


def is_valid_state_name(name: str) -> bool:
    """
    Check if a given string is a valid state name.
    """
    return name.isidentifier()


def is_valid_event_name(name: str) -> bool:
    """
    Check if a given string is a valid event name.
    """
    return name.isidentifier()


def load_yatl_file(file_path: str) -> str:
    """
    Load a YATL file from the given file path.

    :param file_path: Path to the YATL file
    :return: YATL content as a string
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"YATL file not found: {file_path}")

    with open(file_path, "r") as file:
        return file.read()


def process_yatl(yatl_content: str) -> Dict[str, Any]:
    """
    Process YATL content: parse, validate, and compile.

    :param yatl_content: YATL content as a string
    :return: Compiled YATL as a dictionary
    """
    parser = YATLParser()
    validator = YATLValidator()
    compiler = YATLCompiler()

    parsed_yatl = parser.parse(yatl_content)
    if not validator.validate(parsed_yatl):
        raise ValueError(f"YATL validation failed: {validator.errors}")

    compiled_yatl = compiler.compile(parsed_yatl)
    return compiled_yatl


def execute_yatl(compiled_yatl: Dict[str, Any], trigger_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Execute compiled YATL.

    :param compiled_yatl: Compiled YATL as a dictionary
    :param trigger_data: Optional trigger data
    :return: The final context after execution
    """
    runtime = YATLRuntime(compiled_yatl)
    return runtime.execute(trigger_data)


def load_and_execute_yatl(file_path: str, trigger_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Load a YATL file, process it, and execute it.

    :param file_path: Path to the YATL file
    :param trigger_data: Optional trigger data
    :return: The final context after execution
    """
    yatl_content = load_yatl_file(file_path)
    compiled_yatl = process_yatl(yatl_content)
    return execute_yatl(compiled_yatl, trigger_data)


def yatl_from_string(yatl_content: str, trigger_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Process and execute YATL from a string.

    :param yatl_content: YATL content as a string
    :param trigger_data: Optional trigger data
    :return: The final context after execution
    """
    compiled_yatl = process_yatl(yatl_content)
    return execute_yatl(compiled_yatl, trigger_data)
