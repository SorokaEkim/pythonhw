import os
import numpy as np
import pandas as pd
import plotly.express as px


df = pd.read_csv("./lesson8/task1/vgsale_1.csv")

before_2000 = df[df['Year'] < 2000]
after_2000 = df[df['Year'] >= 2000]

# Рассчитываем суммарные продажи по жанрам до 2000 года
sales_before_2000 = before_2000.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().reset_index()

# Рассчитываем суммарные продажи по жанрам после 2000 года
sales_after_2000 = after_2000.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum().reset_index()

# Сортируем данные по общей сумме продаж
sales_before = sales_before_2000.sort_values(by='Global_Sales', ascending=False)
sales_after = sales_after_2000.sort_values(by='Global_Sales', ascending=False)


fig_before = px.bar(sales_before, 
                    x='Genre', 
                    y='Global_Sales', 
                    title='Глобальные продажи игр до 2000 года по жанрам',
                    labels={'Global_Sales': 'Глобальные продажи (в миллионах)', 'Genre': 'Жанр'},
                    color='Global_Sales')

fig_after = px.bar(sales_after, 
                   x='Genre', 
                   y='Global_Sales', 
                   title='Глобальные продажи игр после 2000 года по жанрам',
                   labels={'Global_Sales': 'Глобальные продажи (в миллионах)', 'Genre': 'Жанр'},
                   color='Global_Sales')

fig_before.show()
fig_after.show()

# Группировка данных по жанрам
genre_counts = df['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Game_Count']

# Подсчет глобальных продаж по жанрам
global_sales = df.groupby('Genre')['Global_Sales'].sum().reset_index()
global_sales.columns = ['Genre', 'Total_Global_Sales']

# Объединяем данные
genre_popularity = pd.merge(genre_counts, global_sales, on='Genre')

# Визуализация количества игр по жанрам
fig_game_count = px.bar(genre_popularity,
                         x='Genre',
                         y='Game_Count',
                         title='Количество выпущенных игр по жанрам',
                         labels={'Game_Count': 'Количество игр', 'Genre': 'Жанр'},
                         color='Game_Count')

# Визуализация глобальных продаж по жанрам
fig_sales_count = px.bar(genre_popularity,
                          x='Genre',
                          y='Total_Global_Sales',
                          title='Объем продаж по всему миру по жанрам',
                          labels={'Total_Global_Sales': 'Глобальные продажи (в миллионах)', 'Genre': 'Жанр'},
                          color='Total_Global_Sales')

fig_game_count.show()
fig_sales_count.show()

# Отобрази на графике общее число видеоигр, выпущенных в каждом году.
games_per_year = df['Year'].value_counts().reset_index()
games_per_year.columns = ['Year', 'Number_of_Games']

# Сортируем по году
games_per_year.sort_values('Year', ascending=True, inplace=True)

#Визуализация данных
fig_games_per_year = px.bar(games_per_year, x='Year', y='Number_of_Games', 
             title='Общее число видеоигр, выпущенных в каждом году',
             labels={'Number_of_Games': 'Количество игр', 'Year': 'Год'},
             color='Number_of_Games', 
             color_continuous_scale=px.colors.sequential.Viridis)

# Показываем график
fig_games_per_year.show()

# Определи трех издателей, выпустивших наибольшее количество видеоигр. Изобрази количество выпущенных издателями видеоигр для каждой платформы на столбчатой диаграмме (можно использовать диаграмму с накоплением).
publisher_counts = df['Publisher'].value_counts().reset_index()
publisher_counts.columns = ['Publisher', 'Game_Count']

#Извлечение трех издателей с наибольшим количеством игр
top_publishers = publisher_counts.nlargest(3, 'Game_Count')['Publisher']


# Шаг 4: Подсчет количества игр по платформам для этих издателей
top_publishers_data = df[df['Publisher'].isin(top_publishers)]
platform_counts = top_publishers_data.groupby(['Publisher', 'Platform']).size().reset_index(name='Game_Count')

# Шаг 5: Визуализация данных на столбчатой диаграмме с накоплением
fig = px.bar(platform_counts, 
             x='Platform', 
             y='Game_Count', 
             color='Publisher',
             title='Количество видеоигр, выпущенных тремя крупнейшими издателями по платформам',
             labels={'Game_Count': 'Количество игр', 'Platform': 'Игровая платформа'},
             text='Game_Count')

fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.update_layout(barmode='stack', xaxis_title='Игровая платформа', yaxis_title='Количество игр')

# Показываем график
fig.show()



#Преобразование столбцов с продажами в числовые значения
df['NA_Sales'] = pd.to_numeric(df['NA_Sales'], errors='coerce')
df['EU_Sales'] = pd.to_numeric(df['EU_Sales'], errors='coerce')
df['JP_Sales'] = pd.to_numeric(df['JP_Sales'], errors='coerce')
df['Other_Sales'] = pd.to_numeric(df['Other_Sales'], errors='coerce')
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

#Фильтрация данных по временным периодам
data_pre_2000 = df[df['Year'].between(1980, 2000)]
data_post_2000 = df[df['Year'].between(2000, 2020)]

# Подсчет суммарного объема продаж по регионам для каждого периода
sales_pre_2000 = {
    'North America': data_pre_2000['NA_Sales'].sum(),
    'Europe': data_pre_2000['EU_Sales'].sum(),
    'Japan': data_pre_2000['JP_Sales'].sum(),
    'Other Sales': data_pre_2000['Other_Sales'].sum(),
    'Total Sales': data_pre_2000['Global_Sales'].sum()
}

sales_post_2000 = {
    'North America': data_post_2000['NA_Sales'].sum(),
    'Europe': data_post_2000['EU_Sales'].sum(),
    'Japan': data_post_2000['JP_Sales'].sum(),
    'Other Sales': data_post_2000['Other_Sales'].sum(),
    'Total Sales': data_post_2000['Global_Sales'].sum()
}

# Созование круговых диаграмм
fig_pre_2000 = px.pie(
    names=list(sales_pre_2000.keys())[:-1],  # Исключаем "Total Sales" из названий
    values=list(sales_pre_2000.values())[:-1],  # Исключаем "Total Sales" из значений
    title='Доли суммарного объема продаж (1980-2000)',
    hole=0.4 
)

fig_post_2000 = px.pie(
    names=list(sales_post_2000.keys())[:-1], 
    values=list(sales_post_2000.values())[:-1], 
    title='Доли суммарного объема продаж (2000-2020)',
    hole=0.4 
)

#Отображение диаграмм
fig_pre_2000.show()
fig_post_2000.show()