import unittest

from src.yatl.runtime import YATLRuntime


class TestYATLRuntime(unittest.TestCase):
    def test_execute_task_workflow(self):
        compiled_yatl = {
            "name": "TestWorkflow",
            "description": "A test workflow",
            "initial_state": "Start",
            "states": {"Start": {"type": "task", "action": "sayHello", "next": "End"}, "End": {"type": "end"}},
            "actions": {
                "sayHello": {
                    "description": "Say hello",
                    "language": "python",
                    "code": 'context["greeting"] = "Hello, World!"',
                }
            },
            "variables": {"greeting": "string"},
        }
        runtime = YATLRuntime(compiled_yatl)
        runtime.execute()
        self.assertEqual(runtime.context["greeting"], "Hello, World!")

    def test_execute_choice_workflow(self):
        compiled_yatl = {
            "name": "ChoiceWorkflow",
            "description": "A workflow with a choice",
            "initial_state": "Start",
            "states": {
                "Start": {
                    "type": "choice",
                    "choices": [
                        {
                            "condition": {"variable": "weather", "operator": "equals", "value": "sunny"},
                            "next": "GoOutside",
                        }
                    ],
                    "default": "StayInside",
                },
                "GoOutside": {"type": "end"},
                "StayInside": {"type": "end"},
            },
            "actions": {},
            "variables": {"weather": "string", "activity": "string"},
        }
        runtime = YATLRuntime(compiled_yatl)
        runtime.context["weather"] = "sunny"
        runtime.execute()
        self.assertEqual(runtime.current_state, "GoOutside")

        runtime = YATLRuntime(compiled_yatl)
        runtime.context["weather"] = "rainy"
        runtime.execute()
        self.assertEqual(runtime.current_state, "StayInside")


if __name__ == "__main__":
    unittest.main()
