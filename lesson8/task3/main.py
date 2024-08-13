import os
import numpy as np
import pandas as pd
import plotly.express as px


df = pd.read_csv("./lesson8/task3/shopping_habits.csv")

print(df.head(5))
df['Category'].unique()

# анализ частоты покупок по различным категориям товаров.
category_counts = df['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

fig = px.bar(category_counts, x='Category', y='Count',
             title='Частота покупок по категориям',
             labels={'Count': 'Число покупок', 'Category': 'Категория'},
             color='Count',  # Цвет по числу покупок
             text='Count')  # Подписи на столбцах
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.show()

# распределение рейтингов отзывов относительно времени года

fig = px.box(df, x='Season', y='Review Rating',
             title='Распределение рейтинга отзывов по сезонам',
             labels={'Review Rating': 'Рейтинг отзыва', 'Season': 'Время года'},
             color='Season')  # Цвет по сезонам

fig.show()

gender_amount = df.groupby('Gender')[['Purchase Amount (USD)']].sum().reset_index().sort_values(by='Purchase Amount (USD)', ascending=False)

fig_gender_amount = px.bar(gender_amount, 
    x='Gender', 
    y='Purchase Amount (USD)', 
    title='Зависимость покупок от пола',
    labels={'Purchase Amount (USD)': 'Сумма в USD', 'Gender': 'Пол'},
    color='Gender')

fig_gender_amount.show()