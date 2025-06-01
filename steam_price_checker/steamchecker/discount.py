import requests
from bs4 import BeautifulSoup

def get_max_discount(app_id):
    url = f"https://steamsale.windbell.co.kr/History/{app_id}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    discount_percentages = []
    discount_elements = soup.find_all('td', attrs={'data-v-662ab010': True})
    
    for element in discount_elements:
        text = element.get_text().strip()
        if '%' in text:
            try:
                percent = int(text.replace('%', '').replace('-', '').strip())
                discount_percentages.append(percent)
            except:
                continue

    return max(discount_percentages) if discount_percentages else None