import requests

url = "https://general-runtime.voiceflow.com/state/user/userID/interact?logs=off"

payload = {
    "action": { "type": "launch" },
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

response = requests.post(url, json=payload, headers=headers)

print(response.text)