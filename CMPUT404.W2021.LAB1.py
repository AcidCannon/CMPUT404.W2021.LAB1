import requests
# print version of requests library
# print(requests.__version__)

GOOGLE_HOMEPAGE_URL = "http://google.com/"

req = requests.get(GOOGLE_HOMEPAGE_URL)
print(req.text)

THIS_FILE_URL = "https://raw.githubusercontent.com/AcidCannon/CMPUT404.W2021.LAB1/main/CMPUT404.W2021.LAB1.py"

req = requests.get(THIS_FILE_URL)
print(req.text)