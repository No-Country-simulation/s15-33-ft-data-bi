import requests
import Config
import time

# def obtener_partidos_por_jornada(id_liga, jornada):
#     api_key = Config.token
#     url = f'http://api.football-data.org/v4/competitions/{id_liga}/matches'
#     params = {
#         'matchday': jornada
#     }
#     headers = {
#         'X-Auth-Token': api_key
#     }
#     response = requests.get(url, params=params, headers=headers)
#     partidos = []

#     if response.status_code == 200:
#         data = response.json()
#         if 'matches' in data:
#             for match in data['matches']:
#                 home_team = match['homeTeam']['name']
#                 away_team = match['awayTeam']['name']
#                 match_date = match['utcDate']
#                 partidos.append({'Local': home_team, 'Visitante': away_team, 'Fecha': match_date})
#     return partidos

BASE_URL = "http://api.football-data.org/v4"
headers = {
    'X-Auth-Token': Config.token
}

def get_matches(id, dateFrom=None, dateTo=None, stage=None, status=None, matchday=None, group=None, season=None):
    url = f"{BASE_URL}/competitions/{id}/matches"
    params = {'dateFrom': dateFrom, 'dateTo': dateTo, 'stage': stage, 'status': status, 'matchday': matchday, 'group': group, 'season': season}
    while True:
        response = requests.get(url, params=params, headers=headers)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 429:
                print(f"Rate limit exceeded: {http_err}. Retrying after a pause...")
                time.sleep(60)  # Esperar 60 segundos antes de reintentar
            else:
                print(f"HTTP error occurred: {http_err}")
                break
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            break
        except ValueError:
            print(f"Invalid JSON response: {response.text}")
            break
    return {}

def obtener_partidos_por_jornada(id_liga, jornada):
    data = get_matches(id=id_liga, matchday=jornada)
    partidos = []

    if 'matches' in data:
        for match in data['matches']:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            match_date = match['utcDate']
            partidos.append({
                'Local': home_team, 
                'Visitante': away_team, 
                'Fecha': match_date,
                'Prob_W': ' ',  
                'Prob_D': ' ',
                'Prob_L': ' '
            })
    return partidos


def obtener_tabla_posiciones(id_liga):
    api_key = Config.token
    url = f'http://api.football-data.org/v4/competitions/{id_liga}/standings'
    headers = {
        'X-Auth-Token': api_key
    }
    response = requests.get(url, headers=headers)
    tabla_posiciones = []

    if response.status_code == 200:
        data = response.json()
        if 'standings' in data:
            standings = data['standings'][0]['table']
            for team in standings:
                position = team['position']
                name = team['team']['name']
                played_games = team['playedGames']
                won = team['won']
                draw = team['draw']
                lost = team['lost']
                points = team['points']
                tabla_posiciones.append([position, name, played_games, won, draw, lost, points])
    return tabla_posiciones











