from typing import Any, Dict

import yaml


class YATLParser:
    def __init__(self):
        pass

    def parse(self, yatl_string: str) -> Dict[str, Any]:
        try:
            parsed_data = yaml.safe_load(yatl_string)
            self._validate_structure(parsed_data)
            return parsed_data
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YATL: {str(e)}")

    def _validate_structure(self, data: Dict[str, Any]):
        required_keys = ["name", "description", "initial_state", "states", "actions", "variables"]
        optional_keys = ["version", "triggers"]

        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")

        for key in data.keys():
            if key not in required_keys and key not in optional_keys:
                raise ValueError(f"Unknown key: {key}")

        if not isinstance(data["states"], dict):
            raise ValueError("'states' must be a dictionary")

        if not isinstance(data["actions"], dict):
            raise ValueError("'actions' must be a dictionary")

        if not isinstance(data["variables"], dict):
            raise ValueError("'variables' must be a dictionary")

        if "triggers" in data and not isinstance(data["triggers"], list):
            raise ValueError("'triggers' must be a list")
