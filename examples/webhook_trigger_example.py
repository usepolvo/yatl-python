# webhook_trigger_example.py

from yatl.utils import yatl_from_string

yatl_content = """
name: WebhookTriggerExample
description: "Example of a webhook-triggered workflow"
version: "1.2"
triggers:
  - type: webhook
    event: new_order
    source: ecommerce_system
    auth:
      type: hmac
      secret_env: WEBHOOK_SECRET
initial_state: ProcessOrder

states:
  ProcessOrder:
    type: task
    action: handleNewOrder
    next: End

  End:
    type: task
    action: sendConfirmation
    next: null

actions:
  handleNewOrder:
    description: "Process the new order from the webhook"
    language: python
    code: |
      order = context['trigger']['data']
      context['order_id'] = order['id']
      context['total_amount'] = order['total_amount']
      print(f"Processing new order {context['order_id']} with total ${context['total_amount']}")

  sendConfirmation:
    description: "Send a confirmation message"
    language: python
    code: |
      print(f"Order {context['order_id']} processed successfully")
      context['confirmation_message'] = f"Order {context['order_id']} has been received and is being processed"

variables:
  order_id: string
  total_amount: number
  confirmation_message: string
"""

# In a real scenario, you would set up a webhook receiver to handle the incoming webhook
# and pass the webhook data to the YATL runtime. For this example, we'll simulate a webhook.

simulated_webhook_data = {"id": "12345", "total_amount": 99.99, "items": [{"name": "Widget", "quantity": 2}]}

# Execute the YATL workflow
final_context = yatl_from_string(
    yatl_content,
    trigger_data={
        "type": "webhook",
        "event": "new_order",
        "source": "ecommerce_system",
        "data": simulated_webhook_data,
    },
)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
