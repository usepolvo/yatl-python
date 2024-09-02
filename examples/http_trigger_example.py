# http_trigger_example.py

from yatl.utils import yatl_from_string

yatl_content = """
name: HTTPTriggerExample
description: "Example of an HTTP-triggered workflow"
version: "1.2"
triggers:
  - type: http
    path: /api/greet
    method: POST
    auth:
      type: api_key
      header: X-API-Key
initial_state: ProcessRequest

states:
  ProcessRequest:
    type: task
    action: greetUser
    next: End

  End:
    type: task
    action: returnResponse
    next: null

actions:
  greetUser:
    description: "Greet the user based on the request data"
    language: python
    code: |
      name = context['trigger']['data'].get('name', 'Guest')
      context['greeting'] = f"Hello, {name}!"
      print(context['greeting'])

  returnResponse:
    description: "Prepare the response"
    language: python
    code: |
      context['response'] = {
        'message': context['greeting'],
        'status': 'success'
      }

variables:
  greeting: string
  response: object
"""

# In a real scenario, you would set up a web server to handle the HTTP request
# and pass the request data to the YATL runtime. For this example, we'll simulate a request.

simulated_request_data = {"name": "Alice"}

# Execute the YATL workflow
final_context = yatl_from_string(yatl_content, trigger_data={"type": "http", "data": simulated_request_data})

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")

# In a real scenario, you would return the 'response' as the HTTP response
print("\nHTTP Response:")
print(final_context["response"])
