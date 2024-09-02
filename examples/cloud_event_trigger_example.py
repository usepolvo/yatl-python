# cloud_event_trigger_example.py

from yatl.utils import yatl_from_string

yatl_content = """
name: CloudEventTriggerExample
description: "Example of a cloud event-triggered workflow"
version: "1.2"
triggers:
  - type: cloud_event
    type: com.example.object.created
    source: storage.googleapis.com
initial_state: ProcessNewObject

states:
  ProcessNewObject:
    type: task
    action: handleNewObject
    next: End

  End:
    type: task
    action: logCompletion
    next: null

actions:
  handleNewObject:
    description: "Process the newly created object"
    language: python
    code: |
      event_data = context['trigger']['data']
      context['object_name'] = event_data['name']
      context['bucket_name'] = event_data['bucket']
      print(f"Processing new object: {context['object_name']} in bucket: {context['bucket_name']}")

  logCompletion:
    description: "Log the completion of the workflow"
    language: python
    code: |
      print(f"Finished processing object: {context['object_name']}")
      context['log_message'] = f"Object {context['object_name']} in bucket {context['bucket_name']} processed successfully"

variables:
  object_name: string
  bucket_name: string
  log_message: string
"""

# In a real scenario, this would be triggered by a cloud event system.
# For this example, we'll simulate a cloud event.

simulated_cloud_event_data = {
    "name": "example-object.txt",
    "bucket": "my-gcs-bucket",
    "contentType": "text/plain",
    "size": "1024",
}

# Execute the YATL workflow
final_context = yatl_from_string(
    yatl_content,
    trigger_data={
        "type": "cloud_event",
        "event_type": "com.example.object.created",
        "source": "storage.googleapis.com",
        "data": simulated_cloud_event_data,
    },
)

# Print the final context to see the results
print("\nFinal context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
