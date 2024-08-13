import os
import numpy as np
import pandas as pd
import plotly.express as px


df = pd.read_csv("./lesson8/task2/IQ_countries.csv")

best_continent_iq = df.groupby('Continent')[['Average IQ']].sum().reset_index().sort_values(by='Average IQ', ascending=False)

fig_best_continent_iq = px.bar(best_continent_iq, 
    x='Continent', 
    y='Average IQ', 
    title='Лучшие показатели IQ по континентам',
    labels={'Average IQ': 'Сумма  средних показателей IQ', 'Continent': 'Континет'},
    color='Average IQ')

fig_best_continent_iq.show()


count_nobel_prices = df.groupby('Country')[['Nobel Prices']].sum().reset_index().sort_values(by='Nobel Prices', ascending=False)

fig_count_nobel_prices = px.bar(count_nobel_prices, 
    x='Country', 
    y='Nobel Prices', 
    title='Рейтинг стран по количеству Нобелевских премий',
    labels={'Nobel Prices': 'Количество премий', 'Country': 'Страны'},
    color='Nobel Prices')

fig_count_nobel_prices.show()