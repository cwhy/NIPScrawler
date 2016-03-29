from bs4 import BeautifulSoup as bs
import requests
import json

front_url = "http://papers.nips.cc/book/advances-in-neural-information-processing-systems-28-2015"
base_url = "http://papers.nips.cc/"
res = requests.get(front_url)

soup = bs(res.text)
titleDOMs = soup.findAll("div", class_="main")[0].findAll('li')
title_links = [(e('a')[0].contents[0], e('a')[0]['href']) for e in titleDOMs]

out = []
for (_title, _l) in title_links:
    _res = requests.get(base_url + _l)
    _soup = bs(_res.text)
    abst = _soup.findAll("p", class_="abstract")[0].contents[0]
    out.append((_title, abst))

out_s = [{'title':str(o[0]),'abstract':str(o[1])} for o in out]
with open("log.json", 'w') as _f:
    json.dump(out_s, _f)
