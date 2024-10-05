import requests
import json
from datetime import datetime

def fetch_air_quality_data(city_name, api_key):
    """Fetch air quality data from OpenWeather API."""
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?q={city_name}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except Exception as e:
        print(f"Error: {str(e)}")
    return None

def save_data_to_file(data, city_name):
    """Save the fetched data to a JSON file."""
    filename = f"{city_name}_air_quality_data.json"
    
    # Include a timestamp for when the data was collected
    data['timestamp'] = datetime.now().isoformat()

    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Data saved to {filename}")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeather API key
    city_name = input("Enter the city name to collect air quality data: ")

    data = fetch_air_quality_data(city_name, api_key)
    
    if data:
        save_data_to_file(data, city_name)

if __name__ == '__main__':
    main()
