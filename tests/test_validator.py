import unittest

from src.yatl.validator import YATLValidator


class TestYATLValidator(unittest.TestCase):
    def setUp(self):
        self.validator = YATLValidator()

    def test_validate_valid_yatl(self):
        valid_yatl = {
            "name": "TestWorkflow",
            "description": "A test workflow",
            "initial_state": "Start",
            "states": {"Start": {"type": "task", "action": "sayHello", "next": "End"}, "End": {"type": "end"}},
            "actions": {
                "sayHello": {"description": "Say hello", "language": "python", "code": 'print("Hello, World!")'}
            },
            "variables": {"greeting": "string"},
        }
        self.assertTrue(self.validator.validate(valid_yatl))
        self.assertEqual(len(self.validator.errors), 0)

    def test_validate_invalid_yatl(self):
        invalid_yatl = {
            "name": "InvalidWorkflow",
            "description": "An invalid workflow",
            "initial_state": "NonExistentState",
            "states": {"Start": {"type": "unknown", "next": "End"}, "End": {"type": "end"}},
            "actions": {"missingFields": {}},
            "variables": "not a dictionary",
        }
        self.assertFalse(self.validator.validate(invalid_yatl))
        self.assertGreater(len(self.validator.errors), 0)


if __name__ == "__main__":
    unittest.main()
