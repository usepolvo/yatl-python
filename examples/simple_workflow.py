from yatl.parser import YATLParser
from yatl.compiler import YATLCompiler
from yatl.runtime import YATLRuntime
from yatl.validator import YATLValidator

# Define a simple YATL workflow
yatl_content = """
name: CoffeeMachine
initial_state: Idle
states:
  Idle:
    type: normal
    transitions:
      - event: CoinInserted
        target: Ready
  Ready:
    type: normal
    transitions:
      - event: BrewButtonPressed
        target: Brewing
  Brewing:
    type: normal
    on_enter: [startBrewing]
    on_exit: [stopBrewing]
    transitions:
      - event: BrewingComplete
        target: Idle
"""

# Parse and validate the YATL content
parser = YATLParser()
validator = YATLValidator()
parsed_yatl = parser.parse(yatl_content)

if not validator.validate(parsed_yatl):
    print("YATL validation failed:")
    for error in validator.errors:
        print(f"- {error}")
    exit(1)

# Compile the YATL
compiler = YATLCompiler()
compiled_yatl = compiler.compile(parsed_yatl)

# Create a runtime
runtime = YATLRuntime(compiled_yatl)


# Define action handlers
def start_brewing():
    print("Starting to brew coffee...")


def stop_brewing():
    print("Finished brewing coffee.")


# Register actions
runtime.register_action("startBrewing", start_brewing)
runtime.register_action("stopBrewing", stop_brewing)

# Run the workflow
print(f"Current state: {runtime.current_state}")
runtime.trigger_event("CoinInserted")
print(f"Current state: {runtime.current_state}")
runtime.trigger_event("BrewButtonPressed")
print(f"Current state: {runtime.current_state}")
runtime.trigger_event("BrewingComplete")
print(f"Current state: {runtime.current_state}")
