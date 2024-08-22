# YATL-Python Documentation

Welcome to the documentation for YATL-Python, a Python implementation of YATL (Yet Another Tentacle Language) for defining and managing state machines.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Core Concepts](#core-concepts)
4. [API Reference](api.md)

## Installation

To install YATL-Python, use pip:

```bash
pip install yatl-python
```

## Quick Start

Here's a simple example of how to use YATL-Python:

```python
from yatl.parser import YATLParser
from yatl.compiler import YATLCompiler
from yatl.runtime import YATLRuntime

# Define your YATL content
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
        target: Yellow
  Yellow:
    type: normal
    transitions:
      - event: TimerExpired
        target: Red
"""

# Parse and compile YATL
parser = YATLParser()
compiler = YATLCompiler()
parsed_yatl = parser.parse(yatl_content)
compiled_yatl = compiler.compile(parsed_yatl)

# Create runtime
runtime = YATLRuntime(compiled_yatl)

# Use the state machine
print(runtime.current_state)  # Output: Red
runtime.trigger_event('TimerExpired')
print(runtime.current_state)  # Output: Green
```

## Core Concepts

YATL-Python is based on the following core concepts:

- **States**: Represent the different conditions or modes of a system.
- **Events**: Triggers that cause transitions between states.
- **Transitions**: Define how the system moves from one state to another in response to events.
- **Actions**: Operations that are executed when entering or exiting a state.

For more detailed information, please refer to the [API Reference](api.md).
