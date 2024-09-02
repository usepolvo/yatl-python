from yatl.utils import yatl_from_string

yatl_content = """
name: WeatherChoice
description: "Choose activity based on weather"
version: "1.2"
initial_state: CheckWeather

states:
  CheckWeather:
    type: task
    action: getWeather
    next: DecideActivity

  DecideActivity:
    type: choice
    choices:
      - condition:
          variable: weather
          operator: equals
          value: "sunny"
        next: GoOutside
      - condition:
          variable: weather
          operator: equals
          value: "rainy"
        next: StayInside
    default: StayInside

  GoOutside:
    type: task
    action: planOutdoorActivity
    next: End

  StayInside:
    type: task
    action: planIndoorActivity
    next: End

  End:
    type: task
    action: announceActivity
    next: null

actions:
  getWeather:
    description: "Get the weather"
    language: python
    code: |
      import random
      context['weather'] = random.choice(["sunny", "rainy"])
      print(f"The weather is {context['weather']}")

  planOutdoorActivity:
    description: "Plan outdoor activity"
    language: python
    code: |
      context['activity'] = "go for a walk"

  planIndoorActivity:
    description: "Plan indoor activity"
    language: python
    code: |
      context['activity'] = "read a book"

  announceActivity:
    description: "Announce the activity"
    language: python
    code: |
      print(f"Let's {context['activity']}!")

variables:
  weather: string
  activity: string
"""


# Execute the YATL workflow
final_context = yatl_from_string(yatl_content)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
