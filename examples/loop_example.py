from yatl.utils import yatl_from_string

yatl_content = """
name: NumberSumLoop
description: "Sum a list of numbers"
version: "1.2"
initial_state: InitializeSum

states:
  InitializeSum:
    type: task
    action: initializeVariables
    next: SumNumbers

  SumNumbers:
    type: loop
    collection: numbers
    iterator: currentNumber
    body:
      type: task
      action: addToSum
    next: PrintResult

  PrintResult:
    type: task
    action: printSum
    next: null

actions:
  initializeVariables:
    description: "Initialize variables"
    language: python
    code: |
      context['numbers'] = [1, 2, 3, 4, 5]
      context['sum'] = 0

  addToSum:
    description: "Add current number to sum"
    language: python
    code: |
      context['sum'] += context['currentNumber']

  printSum:
    description: "Print the final sum"
    language: python
    code: |
      print(f"The sum of {context['numbers']} is {context['sum']}")

variables:
  numbers: list
  currentNumber: number
  sum: number
"""


# Execute the YATL workflow
final_context = yatl_from_string(yatl_content)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
