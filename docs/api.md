# YATL-Python API Reference

## YATLParser

The `YATLParser` class is responsible for parsing YATL content into a Python dictionary.

### Methods

#### `parse(yatl_string: str) -> Dict[str, Any]`

Parses a YATL string and returns a dictionary representation.

- **Parameters:**
  - `yatl_string`: A string containing YATL content.
- **Returns:** A dictionary representing the parsed YATL content.
- **Raises:** `ValueError` if the YATL content is invalid.

## YATLCompiler

The `YATLCompiler` class compiles parsed YATL content into a format that can be used by the runtime.

### Methods

#### `compile(parsed_yatl: Dict[str, Any]) -> Dict[str, Any]`

Compiles parsed YATL content into a runtime-ready format.

- **Parameters:**
  - `parsed_yatl`: A dictionary representing parsed YATL content.
- **Returns:** A dictionary representing the compiled YATL content.

## YATLRuntime

The `YATLRuntime
