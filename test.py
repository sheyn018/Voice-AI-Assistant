import requests

url = "https://26370899-f56f-4f55-a300-05ea745cf312-00-1o2ao5xg8awr9.pike.replit.dev/weather"

# Define the query parameters
params = {
    "city": "London",
}

# Send the GET request
response = requests.get(url, params=params)

# Print the response
print(response.status_code)
print(response.json())
