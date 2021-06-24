import time
import requests
import concurrent.futures
from bs4 import BeautifulSoup
# from novel_text_sites import novel_text_sites

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/53.0.2785.143 Safari/537.36'}
MAX_THREADS = 10


def parse(url):
    text = ""
    title = ""
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        time.sleep(2)

        if response.status_code != 200:
            return False

        print('Processing..' + url)
        response.encoding = 'shift_jis'
        soup = BeautifulSoup(response.text, 'html.parser')
        contents = soup.find_all('body')
        if contents is not None:
            for content in contents:
                title = content.find(class_='title').get_text().replace('\n', '')
                text = content.find(class_='main_text').get_text().replace('\n', '')

    except Exception as ex:
        print(str(ex))
    finally:
        with open('new_aozora_text.txt', 'a+', encoding='utf-8') as file:
            file.write("\n" + 'Title: ' + title)
            file.write(text + "\n")


def download_links(card_links):
    threads = min(MAX_THREADS, len(card_links))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(parse, card_links)


def main(story_urls):
    t0 = time.time()
    download_links(story_urls)
    t1 = time.time()
    print(f"{t1 - t0} seconds to download {len(story_urls)} stories.")


# main(novel_text_sites)
