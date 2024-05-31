import requests

url = "https://9e1f21c7-aded-4559-9c59-47cbcbc002e6-00-2jbfkmj4zy90.pike.replit.dev/query"  # Update with the correct URL if running on a different host

# Define the payload with the dynamic question
payload = {
    "question": "I am looking for lodges"
}

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Print the response
print(response.status_code)
print(response.json())
