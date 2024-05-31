import requests
import json

url = "https://general-runtime.voiceflow.com/state/user/userID/interact?logs=off"

payload = {
    "action": {
        "type": "text",
        "payload": "My email is sheane@gmail.com"
    },
    "config": {
        "tts": False,
        "stripSSML": True,
        "stopAll": True,
        "excludeTypes": ["block", "debug", "flow"]
    }
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "VF.DM.65e5c101ad8fa15835b3b768.rwEjVSlwR7vf8PXn"
}

# Assuming you have already defined 'url', 'payload', and 'headers'
response = requests.post(url, json=payload, headers=headers)

# Convert the response JSON to a Python object
response_json = json.loads(response.text)

# Extract all messages from the response
messages = []
for item in response_json:
    if item['type'] == 'text':
        messages.append(item['payload']['message'])

print(messages)