import requests

from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='5e6c5a9a4fbc4555b416b63f407b329c')

# Получить и вывести список последних 10-ти новостей, выпущенных информационным агентством BBC;
top_headlines = newsapi.get_top_headlines(sources='bbc-news')

print('Cписок последних 10-ти новостей:')
for article in top_headlines['articles']:
    print(article['title'])

# Получить и вывести список информационных агентств, публикующих новости на испанском языке;
all_spain_articles = newsapi.get_everything(
                                            q='sport',
                                            language='es',
                                            page_size=10,
                                      )
print('\nCписок информационных агентств, публикующих новости на испанском языке:')
for article in all_spain_articles['articles']:
    print(article['author'])

# Получить и вывести список 5-ти последних новостей связанных с ИИ.
print('\nНовостей связанных с ИИ:')
all_articles_for_ai = newsapi.get_everything(
                                            q='ИИ',
                                            language='ru',
                                            page_size=5,
                                      )
for article in all_articles_for_ai['articles']:
    print(article['title'])