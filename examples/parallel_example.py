from yatl.utils import yatl_from_string

yatl_content = """
name: ParallelTasks
description: "Execute tasks in parallel"
version: "1.2"
initial_state: Start

states:
  Start:
    type: task
    action: initializeTasks
    next: ParallelExecution

  ParallelExecution:
    type: parallel
    branches:
      - type: task
        action: executeTaskA
      - type: task
        action: executeTaskB
    next: End

  End:
    type: task
    action: printResults
    next: null

actions:
  initializeTasks:
    description: "Initialize tasks"
    language: python
    code: |
      import threading
      context['results'] = []
      context['lock'] = threading.Lock()

  executeTaskA:
    description: "Execute Task A"
    language: python
    code: |
      import time
      time.sleep(1)  # Simulate work
      with context['lock']:
        context['results'].append("Task A completed")

  executeTaskB:
    description: "Execute Task B"
    language: python
    code: |
      import time
      time.sleep(2)  # Simulate work
      with context['lock']:
        context['results'].append("Task B completed")

  printResults:
    description: "Print execution results"
    language: python
    code: |
      for result in context['results']:
        print(result)

variables:
  results: list
  lock: object
"""


# Execute the YATL workflow
final_context = yatl_from_string(yatl_content)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
