import requests
from settings import API_URL
# Define the URL of the REST API

def get_data(event_id):
    
    try:
        response = requests.get(API_URL+str(event_id), verify=False)  # Disable SSL verification
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON data from the response
        #print(data)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

    #print(data)
    return data


def parse_data(data):
    # Parse the data and return a list of dictionaries
    parsed_data = []
    for item in data:
        parsed_item = {
            "title": item["title"],
            "barcode": item["barcode"],
            "description": ' '.join(item["description"].replace("\n", "").replace("\r", "").split()),
            "min_players": item["min_players"],
            "max_players": item["max_players"],
            "min_playtime": item["min_playtime"],
            "max_playtime": item["max_playtime"],
            "categories": item["categories"].split("; ") if item["categories"] else [],
            "mechanics": item["mechanics"].split("; ") if item["mechanics"] else [],
        }
        parsed_data.append(parsed_item)

    return parsed_data
    


if __name__ == "__main__":
    data = get_data('27')
    for item in parse_data(data):
        print(item.get("description"))
        print("\n")
    