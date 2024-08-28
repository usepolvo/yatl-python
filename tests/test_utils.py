import unittest
from unittest.mock import mock_open, patch

from src.yatl.utils import (
    execute_yatl,
    is_valid_event_name,
    is_valid_state_name,
    load_and_execute_yatl,
    load_yatl_file,
    process_yatl,
    yatl_from_string,
)


class TestYATLUtils(unittest.TestCase):
    def test_is_valid_state_name(self):
        self.assertTrue(is_valid_state_name("ValidState"))
        self.assertTrue(is_valid_state_name("valid_state"))
        self.assertTrue(is_valid_state_name("_validState"))
        self.assertFalse(is_valid_state_name("1InvalidState"))
        self.assertFalse(is_valid_state_name("Invalid State"))
        self.assertFalse(is_valid_state_name("invalid-state"))

    def test_is_valid_event_name(self):
        self.assertTrue(is_valid_event_name("ValidEvent"))
        self.assertTrue(is_valid_event_name("valid_event"))
        self.assertTrue(is_valid_event_name("_validEvent"))
        self.assertFalse(is_valid_event_name("1InvalidEvent"))
        self.assertFalse(is_valid_event_name("Invalid Event"))
        self.assertFalse(is_valid_event_name("invalid-event"))

    @patch("builtins.open", new_callable=mock_open, read_data="test: data")
    @patch("os.path.exists", return_value=True)
    def test_load_yatl_file(self, mock_exists, mock_file):
        result = load_yatl_file("test.yaml")
        self.assertEqual(result, "test: data")
        mock_file.assert_called_once_with("test.yaml", "r")

    @patch("os.path.exists", return_value=False)
    def test_load_yatl_file_not_found(self, mock_exists):
        with self.assertRaises(FileNotFoundError):
            load_yatl_file("nonexistent.yaml")

    def test_process_yatl(self):
        yatl_content = """
        name: TestWorkflow
        description: "Test workflow"
        initial_state: Start
        states:
          Start:
            type: task
            action: testAction
            next: null
        actions:
          testAction:
            description: "Test action"
            language: python
            code: |
              print("Test")
        variables:
          test: string
        """
        result = process_yatl(yatl_content)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "TestWorkflow")

    def test_process_yatl_invalid(self):
        invalid_yatl = "invalid: yaml: content"
        with self.assertRaises(ValueError):
            process_yatl(invalid_yatl)

    def test_execute_yatl(self):
        compiled_yatl = {
            "name": "TestWorkflow",
            "description": "Test workflow",
            "initial_state": "Start",
            "states": {"Start": {"type": "task", "action": "testAction", "next": None}},
            "actions": {
                "testAction": {
                    "description": "Test action",
                    "language": "python",
                    "code": "context['test'] = 'executed'",
                }
            },
            "variables": {"test": None},
        }
        result = execute_yatl(compiled_yatl)
        self.assertEqual(result["test"], "executed")

    @patch("src.yatl.utils.load_yatl_file")
    @patch("src.yatl.utils.process_yatl")
    @patch("src.yatl.utils.execute_yatl")
    def test_load_and_execute_yatl(self, mock_execute, mock_process, mock_load):
        mock_load.return_value = "test: content"
        mock_process.return_value = {"compiled": "yatl"}
        mock_execute.return_value = {"result": "executed"}

        result = load_and_execute_yatl("test.yaml")
        self.assertEqual(result, {"result": "executed"})
        mock_load.assert_called_once_with("test.yaml")
        mock_process.assert_called_once_with("test: content")
        mock_execute.assert_called_once_with({"compiled": "yatl"})

    @patch("src.yatl.utils.process_yatl")
    @patch("src.yatl.utils.execute_yatl")
    def test_yatl_from_string(self, mock_execute, mock_process):
        mock_process.return_value = {"compiled": "yatl"}
        mock_execute.return_value = {"result": "executed"}

        result = yatl_from_string("test: content")
        self.assertEqual(result, {"result": "executed"})
        mock_process.assert_called_once_with("test: content")
        mock_execute.assert_called_once_with({"compiled": "yatl"})


if __name__ == "__main__":
    unittest.main()
