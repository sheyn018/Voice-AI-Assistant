import requests

url = "https://81f01025-5c17-4234-81bc-ddad6db23482-00-25ibdldge9h6v.pike.replit.dev/query"  # Update with the correct URL if running on a different host

# Define the payload with the dynamic question
payload = {
    "question": "What are the features of the project?"
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
