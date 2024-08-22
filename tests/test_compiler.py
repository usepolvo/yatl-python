from src.yatl.compiler import YATLCompiler


def test_compiler_basic():
    compiler = YATLCompiler()
    parsed_yatl = {
        "name": "TrafficLight",
        "initial_state": "Red",
        "states": {
            "Red": {"type": "normal", "transitions": [{"event": "TimerExpired", "target": "Green"}]},
            "Green": {"type": "normal", "transitions": [{"event": "TimerExpired", "target": "Red"}]},
        },
    }

    compiled_yatl = compiler.compile(parsed_yatl)

    assert compiled_yatl["name"] == "TrafficLight"
    assert compiled_yatl["initial_state"] == "Red"
    assert "Red" in compiled_yatl["states"]
    assert "Green" in compiled_yatl["states"]
    assert compiled_yatl["states"]["Red"]["transitions"]["TimerExpired"] == "Green"
    assert compiled_yatl["states"]["Green"]["transitions"]["TimerExpired"] == "Red"


# Add more tests as needed
