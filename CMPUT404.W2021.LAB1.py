import requests
# print version of requests library
# print(requests.__version__)

GOOGLE_HOMEPAGE_URL = "http://google.com/"

req = requests.get(GOOGLE_HOMEPAGE_URL)
print(req.text)
