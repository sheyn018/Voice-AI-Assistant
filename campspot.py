import requests

def search_room_availability(park_id, checkin, checkout, adults, children, pets):
    base_url = "https://insiderperks.com/wp-content/endpoints/campspot/search-room-available.php"
    
    params = {
        'id': park_id,
        'checkin': checkin,
        'checkout': checkout,
        'adults': adults,
        'children': children,
        'pets': pets
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            print("Response content is not valid JSON:")
            print(response.text)
            # Optionally, return the raw response content as a string
            return response.text
    else:
        response.raise_for_status()

# Example usage
inputVars = {
    'parkId': '92',
    'checkin': '2024-10-06',
    'checkout': '2024-10-08',
    'adults': 2,
    'children': 1,
    'pets': 0,
    'site': 'rv'
}

try:
    availability = search_room_availability(
        inputVars['parkId'],
        inputVars['checkin'],
        inputVars['checkout'],
        inputVars['adults'],
        inputVars['children'],
        inputVars['pets']
    )
    print(availability)
except Exception as e:
    print(f"An error occurred: {e}")
