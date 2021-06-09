import requests
from time import sleep
from bs4 import BeautifulSoup
from novel_text_sites import novel_text_sites

for novel_text_site in novel_text_sites:
    response = requests.get(novel_text_site)
    response.encoding = 'shift_jis'

    soup = BeautifulSoup(response.text, 'html.parser')
    contents = soup.find_all('body')

    title = ""
    text = ""

    try:
        for content in contents:
            title = content.find(class_='title').get_text().replace('\n', '')
            text = content.find(class_='main_text').get_text().replace('\n', '')
    except Exception as err:
        title = err
        text = err

    print(title)
    print(text)

    with open('aozora_text.txt', 'a+', encoding='utf-8') as file:
        try:
            file.write('Title: ' + title + "\n")
            file.write('Text: ' + text + "\n")
        except Exception as err:
            file.write('an ERROR occurred: ' + str(err) + '\n')
    sleep(0.5)
