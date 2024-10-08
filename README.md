# yatl-python

Version: 0.3.1

A Python implementation of 🐙 YATL (Yet Another Tentacle Language) for defining and managing state machines and workflows.

## Introduction

YATL (Yet Another Tentacle Language) is an innovative, octopus-themed markup language designed specifically for defining and managing state machines and workflows. This Python package provides tools to parse, compile, validate, and execute YATL workflows.

## Installation

```bash
pip install yatl-python
```

## Features

- YATL Parser: Converts YATL syntax into an abstract syntax tree (AST)
- YATL Compiler: Transforms the YATL AST into executable code
- YATL Validator: Checks YATL files for syntax and semantic correctness
- YATL Runtime: Executes the compiled YATL workflows
- Trigger System: Supports HTTP, Webhook, Schedule, and Cloud Event triggers

## Usage

Here's a simple example of how to use yatl-python with YATL 1.2 features:

```python
from yatl.parser import YATLParser
from yatl.compiler import YATLCompiler
from yatl.validator import YATLValidator
from yatl.runtime import YATLRuntime

# YATL content
yatl_content = """
name: SimpleWorkflow
description: "A simple workflow example with a schedule trigger"
version: "1.2"
triggers:
  - type: schedule
    cron: "0 * * * *"  # Run every hour
initial_state: Start

states:
  Start:
    type: task
    action: sayHello
    next: Middle

  Middle:
    type: task
    action: sayWorking
    next: End

  End:
    type: task
    action: sayGoodbye
    next: null

actions:
  sayHello:
    description: "Say hello"
    language: python
    code: |
      print(f"Hello! Triggered at {context['trigger']['timestamp']}")

  sayWorking:
    description: "Say working"
    language: python
    code: |
      print("Working...")

  sayGoodbye:
    description: "Say goodbye"
    language: python
    code: |
      print("Goodbye!")

variables:
  dummy: string
"""

# Parse YATL
parser = YATLParser()
parsed_yatl = parser.parse(yatl_content)

# Validate YATL
validator = YATLValidator()
if not validator.validate(parsed_yatl):
    print("Validation errors:", validator.errors)
    exit(1)

# Compile YATL
compiler = YATLCompiler()
compiled_yatl = compiler.compile(parsed_yatl)

# Execute YATL
runtime = YATLRuntime(compiled_yatl)
runtime.execute(trigger_data={"type": "schedule", "timestamp": "2023-06-01T12:00:00Z"})
```

## Advanced Features

YATL 1.2 supports various state types, control structures, and triggers:

- Task States
- Choice States
- Loop States
- Parallel States
- End States
- Fail States
- Triggers: HTTP, Webhook, Schedule, Cloud Event

For more detailed examples and usage of these features, please refer to the [docs](docs/) directory.

## Development

To set up the development environment:

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest tests/`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [usepolvo](https://github.com/usepolvo/usepolvo): The main usepolvo project, an open-source API integration toolkit
- [yatl-node](https://github.com/usepolvo/yatl-node): Node.js implementation of YATL
- [yatl-java](https://github.com/usepolvo/yatl-java): Java implementation of YATL
- [yatl-go](https://github.com/usepolvo/yatl-go): Go implementation of YATL

For more information about YATL and its ecosystem, visit the [YATL Specification](https://github.com/usepolvo/yatl-core/blob/main/specification/yatl-spec.md).
