from yatl.utils import yatl_from_string

yatl_content = """
name: PizzaOrderingSystem
description: "A comprehensive pizza ordering system using YATL"
initial_state: WelcomeCustomer

states:
  WelcomeCustomer:
    type: task
    action: greetCustomer
    next: TakeOrder

  TakeOrder:
    type: loop
    collection: menu_items
    iterator: current_item
    body:
      type: choice
      choices:
        - condition:
            variable: current_item
            operator: equals
            value: "pizza"
          next: OrderPizza
        - condition:
            variable: current_item
            operator: equals
            value: "drink"
          next: OrderDrink
      default: SkipItem
    next: ConfirmOrder

  OrderPizza:
    type: task
    action: addPizzaToOrder
    next: null

  OrderDrink:
    type: task
    action: addDrinkToOrder
    next: null

  SkipItem:
    type: task
    action: skipMenuItem
    next: null

  ConfirmOrder:
    type: choice
    choices:
      - condition:
          variable: order_total
          operator: greater_than
          value: 0
        next: ProcessPayment
    default: CancelOrder

  ProcessPayment:
    type: parallel
    branches:
      - type: task
        action: processPayment
      - type: task
        action: preparePizzas
    next: DeliverOrder

  CancelOrder:
    type: task
    action: cancelEmptyOrder
    next: End

  DeliverOrder:
    type: task
    action: deliverOrder
    next: End

  End:
    type: task
    action: thankCustomer
    next: null

actions:
  greetCustomer:
    description: "Welcome the customer"
    language: python
    code: |
      print("Welcome to YATL Pizza!")
      context['customer_name'] = input("What's your name? ")
      print(f"Hello, {context['customer_name']}!")
      context['menu_items'] = ['pizza', 'drink']
      context['order'] = []
      context['order_total'] = 0

  addPizzaToOrder:
    description: "Add a pizza to the order"
    language: python
    code: |
      pizza_type = input("What type of pizza would you like? ")
      context['order'].append(f"{pizza_type} pizza")
      context['order_total'] += 10
      print(f"{pizza_type} pizza added to your order.")

  addDrinkToOrder:
    description: "Add a drink to the order"
    language: python
    code: |
      drink_type = input("What type of drink would you like? ")
      context['order'].append(f"{drink_type} drink")
      context['order_total'] += 2
      print(f"{drink_type} drink added to your order.")

  skipMenuItem:
    description: "Skip the current menu item"
    language: python
    code: |
      print(f"Skipping {context['current_item']}.")

  processPayment:
    description: "Process the payment for the order"
    language: python
    code: |
      print(f"Processing payment of ${context['order_total']}...")
      import time
      time.sleep(2)
      print("Payment processed successfully!")

  preparePizzas:
    description: "Prepare the pizzas for the order"
    language: python
    code: |
      print("Preparing your order...")
      import time
      for item in context['order']:
        if 'pizza' in item:
          print(f"Baking {item}...")
          time.sleep(3)
      print("Order prepared!")

  cancelEmptyOrder:
    description: "Cancel an empty order"
    language: python
    code: |
      print("Your order is empty. Order cancelled.")

  deliverOrder:
    description: "Deliver the completed order"
    language: python
    code: |
      print(f"Delivering your order to {context['customer_name']}:")
      for item in context['order']:
        print(f"- {item}")
      print(f"Total: ${context['order_total']}")

  thankCustomer:
    description: "Thank the customer for their order"
    language: python
    code: |
      print(f"Thank you for your order, {context['customer_name']}! Enjoy your meal!")

variables:
  customer_name: string
  menu_items: list
  current_item: string
  order: list
  order_total: number
"""

# Execute the YATL workflow
final_context = yatl_from_string(yatl_content)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    if key != "lock":  # Skip printing the lock object
        print(f"{key}: {value}")
