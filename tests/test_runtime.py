from src.yatl.runtime import YATLRuntime


def test_runtime_basic():
    compiled_yatl = {
        "name": "TrafficLight",
        "initial_state": "Red",
        "states": {
            "Red": {
                "type": "normal",
                "on_enter": ["turnOnRed"],
                "on_exit": ["turnOffRed"],
                "transitions": {"TimerExpired": "Green"},
            },
            "Green": {
                "type": "normal",
                "on_enter": ["turnOnGreen"],
                "on_exit": ["turnOffGreen"],
                "transitions": {"TimerExpired": "Red"},
            },
        },
    }

    runtime = YATLRuntime(compiled_yatl)

    assert runtime.current_state == "Red"

    actions_executed = []

    def turn_on_red():
        actions_executed.append("turnOnRed")

    def turn_off_red():
        actions_executed.append("turnOffRed")

    def turn_on_green():
        actions_executed.append("turnOnGreen")

    runtime.register_action("turnOnRed", turn_on_red)
    runtime.register_action("turnOffRed", turn_off_red)
    runtime.register_action("turnOnGreen", turn_on_green)

    runtime.trigger_event("TimerExpired")

    assert runtime.current_state == "Green"
    assert actions_executed == ["turnOffRed", "turnOnGreen"]


# Add more tests as needed
