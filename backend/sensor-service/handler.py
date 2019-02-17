import boto3
import json
import logging
import logging.config

client = boto3.client('iot-data', region_name='us-east-1')

def load_log_config():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    return root

# Load logging config and create logger
logger = load_log_config()

def process_data(event, context):
  print(json.dumps(event['body'], indent=2))
  data = json.loads(event['body'])
  print('Data ' + json.dumps(data))
  # Change topic, qos and payload
  response = client.publish(
        topic='sensordata',
        qos=1,
        payload=json.dumps(data).encode('utf-8')
    )
  print('Response ' + str(response))
  
  return {
    "statusCode": 200,
     "headers": {
        "Content-Type": "application/json"
     },
     "body": ""
  }
