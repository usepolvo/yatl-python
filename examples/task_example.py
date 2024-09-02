from yatl.utils import yatl_from_string

yatl_content = """
name: SimpleTaskWorkflow
description: "Demonstrate basic task states"
version: "1.2"
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
      print("Hello!")
      context['greeting'] = "Hello!"

  sayWorking:
    description: "Say working"
    language: python
    code: |
      print("Working...")
      context['status'] = "working"

  sayGoodbye:
    description: "Say goodbye"
    language: python
    code: |
      print("Goodbye!")
      context['farewell'] = "Goodbye!"

variables:
  greeting: string
  status: string
  farewell: string
"""

# Execute the YATL workflow
final_context = yatl_from_string(yatl_content)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
