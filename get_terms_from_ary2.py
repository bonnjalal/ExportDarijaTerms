# import pywikibot
# from pywikibot import families
#
# site = pywikibot.Site("incubator","incubator")
#
# page = pywikibot.Page(site, "Wt/ary")
# print(page)


import requests

S = requests.Session()

URL = "https://incubator.wikimedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "apfrom": "Wt/ary/",
    "aplimit":2000,
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["allpages"]

# print(DATA)
for page in PAGES:
    print(page["title"])
