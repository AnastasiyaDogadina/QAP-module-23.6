import requests
import os

DOMAIN = 'https://min-api.cryptocompare.com/data/'


def get_sys_list():
    url = '{DOMAIN}blockchain/list?api_key={KEY}'.format(DOMAIN=DOMAIN, KEY=os.getenv('CRYPTO_API_KEY'))
    r = requests.get(url).json()
    return [r['Data'][i]['symbol'] for i in r['Data']]


def single_price(from_symbol, to_symbol):
    url = '{DOMAIN}price?fsym={FROM}&tsyms={TO}&api_key={KEY}'.format(
        DOMAIN=DOMAIN,
        FROM=from_symbol,
        TO=to_symbol,
        KEY=os.getenv('CRYPTO_API_KEY')
    )
    r = requests.get(url).json()
    try:
        return r[list(r.keys())[0]]
    except Exception as err:
        print(err)
        return None
