import re
import time
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from aozora_card_sites import aozora_card_sites

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.143 Safari/537.36'}
MAX_THREADS = 10


def parse(url):
    url_string_format = ''
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        time.sleep(2)

        if response.status_code != 200:
            return False

        print('Processing..' + url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        contents = soup.find('a', text=re.compile("いますぐ.*読む"))
        if contents is not None:
            novel_text_url = re.sub('/card[0-9]*.html', contents['href'][1:], url)
            url_string_format = '"' + novel_text_url + '",'

    except Exception as ex:
        print(str(ex))
    finally:
        with open('new_novel_text_sites.py', 'a+') as file:
            file.write(url_string_format + "\n")


def download_links(card_links):
    threads = min(MAX_THREADS, len(card_links))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(parse, card_links)


def main(story_urls):
    t0 = time.time()
    download_links(story_urls)
    t1 = time.time()
    print(f"{t1-t0} seconds to download {len(story_urls)} stories.")


main(aozora_card_sites)