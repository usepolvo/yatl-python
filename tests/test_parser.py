import pytest

from src.yatl.parser import YATLParser


def test_parser_basic():
    parser = YATLParser()
    yatl_content = """
    name: TrafficLight
    initial_state: Red
    states:
      Red:
        type: normal
        transitions:
          - event: TimerExpired
            target: Green
      Green:
        type: normal
        transitions:
          - event: TimerExpired
            target: Red
    """
    parsed_yatl = parser.parse(yatl_content)

    assert parsed_yatl["name"] == "TrafficLight"
    assert parsed_yatl["initial_state"] == "Red"
    assert "Red" in parsed_yatl["states"]
    assert "Green" in parsed_yatl["states"]
    assert parsed_yatl["states"]["Red"]["transitions"][0]["event"] == "TimerExpired"
    assert parsed_yatl["states"]["Red"]["transitions"][0]["target"] == "Green"


def test_parser_invalid_yaml():
    parser = YATLParser()
    invalid_yatl = """
    name: InvalidYAML
    initial_state: Red
    states:
      - This is not valid YAML
    """
    with pytest.raises(ValueError):
        parser.parse(invalid_yatl)


# Add more tests as needed
