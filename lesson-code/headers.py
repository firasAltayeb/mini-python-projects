from requests_html import HTMLSession
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.5",
    "Referer": "https://google.com",
    "Dnt": "1",
}
URL = "https://httpbin.org/headers"
s = HTMLSession()

r = requests.get('https://httpbin.org/headers')
# rh = s.get('https://httpbin.org/headers')
#
# print(r.text)
# print(rh.text)

response = requests.get(URL, headers=HEADERS, timeout=5)

print(response.text)
