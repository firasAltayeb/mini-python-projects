from selenium import webdriver
from bs4 import BeautifulSoup
import concurrent.futures
import requests
import time

URL = 'https://pub.dev'
MAX_THREADS = 10
sub_pages = []


# used when dealing with webpages that need JS to load
# DRIVER = webdriver.Safari()

def parse_main_page():
    # soup = BeautifulSoup(driver.get(URL).page_source, 'html.parser')
    response = requests.get(URL, timeout=5)

    soup = BeautifulSoup(response.text, 'html.parser')

    # for element in soup.find_all(id="ResultsContainer"):
    for element in soup.find_all(attrs={'class': 'mini-list-item'}):
        page_extension = element.find('a')['href']
        if page_extension is not None:
            # gather_dependencies(URL + page_extension)
            sub_pages.append(URL + page_extension)

    # threads = min(MAX_THREADS, len(sub_pages))
    #
    # with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
    #     executor.map(gather_dependencies, sub_pages)


def gather_dependencies(url):
    print(f"popular package {url}")
    print("Dependencies:")
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')

    contents = soup.find_all(attrs={'class': 'detail-info-box'})
    if contents is not None:
        for element in contents:
            for a_element in element.find_all('a', title=True):
                print(a_element['href'])


def main():
    t0 = time.time()
    parse_main_page()
    t1 = time.time()
    print(f"{t1 - t0} seconds to scrape {len(sub_pages)} pages.")


main()
