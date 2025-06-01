import requests

def get_app_id_from_name(game_name):
    search_url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"
    response = requests.get(search_url)
    data = response.json()

    app_list = data['applist']['apps']
    for game in app_list:
        if game_name.lower() == game['name'].lower():
            return game['appid']
    return None