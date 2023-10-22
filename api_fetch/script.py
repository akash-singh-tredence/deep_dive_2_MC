from decouple import config
import requests

def fetch_data(api_key):
    api_url = f'https://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}'

    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    api_key = config('API_KEY')
    fetch_data(api_key)
