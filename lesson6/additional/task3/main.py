import wikipedia

article = wikipedia.page("Python (programming language)")

print(f'Заголовок статьи: {article.title}')
print(f'Содержимое статьи: {article.content[:40]}...')

wikipedia.set_lang('ru')

article = wikipedia.page("Python")
print(f'Заголовок статьи: {article.title}')
print(f'Заголовок статьи: {article.content[:140]}')
