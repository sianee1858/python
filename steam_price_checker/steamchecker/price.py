import requests

API_KEY = '여기에_네_API_키_입력' 

def get_game_price(app_id):
    url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&cc=kr&l=korean&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data[str(app_id)]['success']:
        game_data = data[str(app_id)]['data']
        price_info = game_data.get('price_overview')

        print(f"\n🎮 게임 이름: {game_data['name']}")
        if price_info:
            print(f"💰 현재 가격: {price_info['final_formatted']}")
            print(f"💸 정가: {price_info['initial_formatted']}")
            print(f"📉 현재 할인율: {price_info['discount_percent']}%")
        else:
            print("🔓 무료 게임이거나 가격 정보가 없습니다.")
    else:
        print("❌ 게임 정보를 불러오지 못했습니다.")