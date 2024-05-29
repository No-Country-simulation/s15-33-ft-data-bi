import requests
import Config


api_key = Config.token
url = 'https://api.football-data.org/v4/competitions'
headers = {
    'Authorization': f'Bearer {api_key}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for competition in data['competitions']:
        print(f"ID: {competition['id']}, Nombre: {competition['name']}")
else:
    print("Error:", response.status_code, response.text)