"""
Python Package Manager pip

pip install requests
am Standort:
pip install --proxy=<u><link=http://proxywbs:3128>http://proxywbs:3128</link></u> requests

Pakete auflisten:
pip freeze

"""


import requests

STANDORT = False
proxy = {}

# nur am Standort
if STANDORT:
    proxy = {
        "http": "http://proxywbs:3128",
        "htpps": "http://proxywbs:3128",
    }

r = requests.get("https://www.tagesschau.de", proxies=proxy)
print(r.text, type(r.text))



with open("schrott.txt", mode="w", encoding="utf-8") as f:
    f.write(r.text)