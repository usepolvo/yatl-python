import unittest

from src.yatl.parser import YATLParser


class TestYATLParser(unittest.TestCase):
    def setUp(self):
        self.parser = YATLParser()

    def test_parse_valid_yatl(self):
        valid_yatl = """
        name: TestWorkflow
        description: "A test workflow"
        initial_state: Start
        states:
          Start:
            type: task
            action: sayHello
            next: End
          End:
            type: end
        actions:
          sayHello:
            description: "Say hello"
            language: python
            code: |
              print("Hello, World!")
        variables:
          greeting: string
        """
        parsed = self.parser.parse(valid_yatl)
        self.assertEqual(parsed["name"], "TestWorkflow")
        self.assertEqual(parsed["initial_state"], "Start")
        self.assertIn("Start", parsed["states"])
        self.assertIn("sayHello", parsed["actions"])

    def test_parse_invalid_yatl(self):
        invalid_yatl = """
        name: InvalidWorkflow
        # Missing required keys
        """
        with self.assertRaises(ValueError):
            self.parser.parse(invalid_yatl)


if __name__ == "__main__":
    unittest.main()
