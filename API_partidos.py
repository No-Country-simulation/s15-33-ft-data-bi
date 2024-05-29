import requests
import Config

def obtener_partidos(fecha_desde, fecha_hasta, id_liga):
    api_key = Config.token
    url = 'http://api.football-data.org/v4/matches'
    params = {
        'dateFrom': fecha_desde,
        'dateTo': fecha_hasta,
        'competitions': id_liga
    }
    headers = {
        'X-Auth-Token': api_key
    }
    response = requests.get(url, params=params, headers=headers)
    partidos = []

    if response.status_code == 200:
        data = response.json()
        if 'matches' in data:
            for match in data['matches']:
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                match_date = match['utcDate']
                partidos.append({'Local': home_team, 'Visitante': away_team, 'Fecha': match_date})
    return partidos









