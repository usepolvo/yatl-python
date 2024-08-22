from src.yatl.validator import YATLValidator


def test_validator_valid_yatl():
    validator = YATLValidator()
    valid_yatl = {
        "name": "TrafficLight",
        "initial_state": "Red",
        "states": {
            "Red": {"type": "normal", "transitions": [{"event": "TimerExpired", "target": "Green"}]},
            "Green": {"type": "normal", "transitions": [{"event": "TimerExpired", "target": "Red"}]},
        },
    }

    assert validator.validate(valid_yatl) == True
    assert len(validator.errors) == 0


def test_validator_invalid_yatl():
    validator = YATLValidator()
    invalid_yatl = {
        "name": "InvalidTrafficLight",
        "initial_state": "Purple",  # Invalid initial state
        "states": {
            "Red": {"transitions": [{"event": "TimerExpired", "target": "Green"}]},  # Missing 'type'
            "Green": {"type": "normal", "transitions": "not a list"},  # Invalid transitions format
        },
    }

    assert validator.validate(invalid_yatl) == False
    assert len(validator.errors) > 0


# Add more tests as needed
