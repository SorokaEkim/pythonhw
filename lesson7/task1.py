from requests import get
import pandas as pd
import numpy as np
import os
import warnings
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import ast


warnings.filterwarnings('ignore')

FILE_PATH = './lesson7/the_movies_dataset'

df = pd.read_csv(f'{FILE_PATH}/movies_metadata.csv')
df = df.drop(['imdb_id'], axis=1)
df = df.drop(['adult'], axis=1)
df = df.drop(['belongs_to_collection'], axis=1)
df = df.drop(['homepage'], axis=1)
df = df.drop(['video'], axis=1)
df = df.drop(['poster_path'], axis=1)
df = df.drop(['production_companies'], axis=1)

df['revenue'] = df['revenue'].replace(0, np.nan)
df['budget'] = pd.to_numeric(df['budget'], errors='coerce') # Пытаемся преобразовать в число, в случае ошибки принуждаем (coerce) к NaN
df['budget'] = df['budget'].replace(0, np.nan) # Заменяем 0 на NaN
df[df['budget'].isnull()].shape # Получаем только записи с numpy.NaN или Python None

df['year'] = pd.to_datetime(df['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)
df['return'] = df['revenue'] /  df['budget'] * 100
df[df['return'].notnull()].shape

# #Большинство фильмов выпускаются по пятницам
# df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
# df['weekday'] = df['release_date'].dt.weekday
# df['weekday_name'] = df['release_date'].dt.day_name()
# week_df = pd.DataFrame(df['weekday_name'].value_counts())
# week_df['week_day'] = week_df.index
# week_df.columns = ['count', 'week_day']

# plt.figure(figsize=(12,5)) # Задаем в дюймах область рисования графика (ширина, высота)
# sns.barplot(x='week_day', y='count', data=week_df) # рисуем столбчатый график (категория - значение)
# plt.show()


#Известные актеры снимаются в самых кассовых фильмах

FILE_PATH = './lesson7/the_movies_dataset'
сredit_df = pd.read_csv(f'{FILE_PATH}/credits.csv')

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

df['id'] = df['id'].apply(convert_int)  # Преобразуем к int
df = df.drop(df[df['id'].isnull()].index)
df['id'] = df['id'].astype('int')

df_merge = df.merge(сredit_df, on='id')
df_merge['cast'] = df_merge['cast'].apply(ast.literal_eval)


def get_actor(x):
    for i in x:
        if i['order'] == 0:
            return i['name']
    return np.nan

df_merge['actor_main'] = df_merge['cast'].apply(get_actor)

plt.title('Актеры с лучшими показателями по кассовым сборам')
df_merge.groupby('actor_main').sum().sort_values('revenue', ascending=False)['revenue'].head(10).plot(kind='bar')
plt.show()

plt.title('Актеры в дорогтх фильмах')
df_merge.groupby('actor_main').sum().sort_values('budget', ascending=False)['budget'].head(10).plot(kind='bar')
plt.show()




