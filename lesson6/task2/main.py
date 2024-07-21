from bs4 import BeautifulSoup
import requests

url = ("https://2051.vision/category/ii/") # Зададим адрес новостного сайта для GET-запроса библиотеки requests
html = requests.get(url).text # Извлекаем из тела ответа текстовые данные
soup = BeautifulSoup(html, 'html5lib') # Применяем к данным анализатор html5lib

title_news = soup.find_all('h3', class_='entry-title')
filteredNews = []

for data in title_news:
    if data.find('a') is not None:
        filteredNews.append(data.text.strip())

for title in filteredNews:
    print(title)