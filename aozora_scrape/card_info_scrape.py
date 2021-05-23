import re
import requests
from time import sleep
from bs4 import BeautifulSoup
from aozora_card_sites import aozora_card_sites

for info_card_site in aozora_card_sites:
    response = requests.get(info_card_site)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')
    contents = soup.find('a', text=re.compile("いますぐ.*読む"))

    novel_text_url = re.sub('/card[0-9]*.html', contents['href'][1:], info_card_site)
    url_string_format = '"' + novel_text_url + '",'
    with open('aozora_text_sites.py', 'a+') as file:
        try:
            file.write(url_string_format + '\n')
        except Exception as err:
            file.write('an ERROR occurred: ' + str(err) + '\n')
    print(url_string_format)
    sleep(0.1)
