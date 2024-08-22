# yatl-python

Version: 0.1.2

A Python implementation of 🦑 YATL (Yet Another Tentacle Language) for defining and managing state machines.

## Installation

```bash
pip install yatl
```

## Usage

Here's a simple example of how to use yatl-python:

```python
from yatl.parser import YATLParser
from yatl.compiler import YATLCompiler
from yatl.runtime import YATLRuntime

# YATL content
yatl_content = """
name: TrafficLight
initial_state: Red
states:
  Red:
    type: normal
    on_enter: [turnOnRed]
    transitions:
      - event: TimerExpired
        target: Green
  Green:
    type: normal
    on_enter: [turnOnGreen]
    transitions:
      - event: TimerExpired
        target: Yellow
  Yellow:
    type: normal
    on_enter: [turnOnYellow]
    transitions:
      - event: TimerExpired
        target: Red
"""

# Parse and compile YATL
parser = YATLParser()
compiler = YATLCompiler()
parsed_yatl = parser.parse(yatl_content)
compiled_yatl = compiler.compile(parsed_yatl)

# Create runtime and register actions
runtime = YATLRuntime(compiled_yatl)

def turn_on_red():
    print("Red light on")

def turn_on_green():
    print("Green light on")

def turn_on_yellow():
    print("Yellow light on")

runtime.register_action('turnOnRed', turn_on_red)
runtime.register_action('turnOnGreen', turn_on_green)
runtime.register_action('turnOnYellow', turn_on_yellow)

# Run the state machine
print(f"Current state: {runtime.current_state}")
runtime.trigger_event('TimerExpired')
print(f"Current state: {runtime.current_state}")
runtime.trigger_event('TimerExpired')
print(f"Current state: {runtime.current_state}")
runtime.trigger_event('TimerExpired')
print(f"Current state: {runtime.current_state}")
```

For more detailed documentation, please refer to the [docs](docs/) directory.

## Development

To set up the development environment:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest tests/`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
