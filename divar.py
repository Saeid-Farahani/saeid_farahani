import requests
from bs4 import BeautifulSoup as bs

auto_kind = input('نوع ماشین: ').strip()

if auto_kind:
    payload = {'q': auto_kind}
else:
    raise ValueError("باید نوع ماشین مشخص شود")

def requester(url, pload):

    resp = requests.get(url, params=pload)
    if resp:
        return resp.content
    return None

page = requester('https://divar.ir/s/tehran/car', payload)

if page is not None:
    bsobj = bs(page, 'html.parser')
    car_info = [ x.text
     for x in bsobj.find_all('div', class_='kt-post-card__description')
     ]
    prices = [y.split('\n')[1] for y in car_info]
    for price in prices:
        print(price)
