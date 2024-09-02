# schedule_trigger_example.py

from yatl.utils import yatl_from_string
from datetime import datetime

yatl_content = """
name: ScheduleTriggerExample
description: "Example of a schedule-triggered workflow"
version: "1.2"
triggers:
  - type: schedule
    cron: "0 0 * * *"  # Run daily at midnight
initial_state: PerformDailyTask

states:
  PerformDailyTask:
    type: task
    action: runDailyReport
    next: End

  End:
    type: task
    action: notifyCompletion
    next: null

actions:
  runDailyReport:
    description: "Generate daily report"
    language: python
    code: |
      import random
      context['report_date'] = context['trigger']['timestamp']
      context['daily_metric'] = random.randint(100, 1000)
      print(f"Generating daily report for {context['report_date']}")
      print(f"Daily metric: {context['daily_metric']}")

  notifyCompletion:
    description: "Notify that the daily task is complete"
    language: python
    code: |
      print(f"Daily task completed. Report generated for {context['report_date']}")
      context['notification'] = f"Daily report for {context['report_date']} is ready. Metric: {context['daily_metric']}"

variables:
  report_date: string
  daily_metric: number
  notification: string
"""

# In a real scenario, this would be triggered by a scheduler.
# For this example, we'll simulate a scheduled execution.

simulated_schedule_data = {"timestamp": datetime.now().isoformat()}

# Execute the YATL workflow
final_context = yatl_from_string(
    yatl_content, trigger_data={"type": "schedule", "timestamp": simulated_schedule_data["timestamp"]}
)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
