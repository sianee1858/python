from steamchecker.search import get_app_id_from_name
from steamchecker.price import get_game_price
from steamchecker.discount import get_max_discount

def main():
    game_name = input("🎮 게임 이름을 입력하세요: ")
    app_id = get_app_id_from_name(game_name)

    if app_id:
        print(f"\n🔍 App ID: {app_id}")
        get_game_price(app_id)

        max_discount = get_max_discount(app_id)
        if max_discount is not None:
            print(f"\n📈 역대 최대 할인율: {max_discount}%")
        else:
            print("❌ 할인 이력을 가져올 수 없습니다.")
    else:
        print("❌ 해당 게임을 찾을 수 없습니다. 이름을 다시 확인해주세요.")

if __name__ == "__main__":
    main()