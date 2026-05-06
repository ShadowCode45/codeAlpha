import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/s?k=mobile"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    products = soup.find_all("div", {"data-component-type": "s-search-result"})

    for product in products[:5]:
        name = product.h2.text.strip()
        
        price = product.find("span", "a-price-whole")
        rating = product.find("span", "a-icon-alt")

        print("Name:", name)
        print("Price:", price.text if price else "N/A")
        print("Rating:", rating.text if rating else "N/A")
        print("-" * 50)
else:
    print("Website not accessible")