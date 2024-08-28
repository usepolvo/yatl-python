import unittest

from src.yatl.compiler import YATLCompiler


class TestYATLCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = YATLCompiler()

    def test_compile_task_state(self):
        parsed_yatl = {
            "name": "TestWorkflow",
            "description": "A test workflow",
            "initial_state": "Start",
            "states": {"Start": {"type": "task", "action": "sayHello", "next": "End"}, "End": {"type": "end"}},
            "actions": {
                "sayHello": {"description": "Say hello", "language": "python", "code": 'print("Hello, World!")'}
            },
            "variables": {"greeting": "string"},
        }
        compiled = self.compiler.compile(parsed_yatl)
        self.assertEqual(compiled["name"], "TestWorkflow")
        self.assertIn("Start", compiled["states"])
        self.assertEqual(compiled["states"]["Start"]["type"], "task")
        self.assertEqual(compiled["states"]["Start"]["action"], "sayHello")

    def test_compile_choice_state(self):
        parsed_yatl = {
            "name": "ChoiceWorkflow",
            "description": "A workflow with a choice",
            "initial_state": "Start",
            "states": {
                "Start": {
                    "type": "choice",
                    "choices": [
                        {
                            "condition": {"variable": "$.weather", "operator": "equals", "value": "sunny"},
                            "next": "GoOutside",
                        }
                    ],
                    "default": "StayInside",
                },
                "GoOutside": {"type": "end"},
                "StayInside": {"type": "end"},
            },
            "actions": {},
            "variables": {"weather": "string"},
        }
        compiled = self.compiler.compile(parsed_yatl)
        self.assertIn("Start", compiled["states"])
        self.assertEqual(compiled["states"]["Start"]["type"], "choice")
        self.assertIn("choices", compiled["states"]["Start"])
        self.assertEqual(compiled["states"]["Start"]["default"], "StayInside")


if __name__ == "__main__":
    unittest.main()
