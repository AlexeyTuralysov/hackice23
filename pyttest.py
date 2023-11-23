from bs4 import BeautifulSoup
import requests

# Загрузка HTML-страницы с веб-сайта
url = 'https://example.com'
response = requests.get(url)
html_content = response.content

# Создание объекта BeautifulSoup для парсинга страницы
soup = BeautifulSoup(html_content, 'html.parser')

# Пример: извлечение заголовка страницы
title = soup.title.text
print(f'Title: {title}')

# Пример: извлечение всех ссылок на странице
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# Пример: извлечение текста из определенного элемента
paragraph = soup.find('p')
print(f'Paragraph Text: {paragraph.text}')
