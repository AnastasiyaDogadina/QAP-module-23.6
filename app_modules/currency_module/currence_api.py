import requests
from enum import Enum


# Попыталась сделать аналогично классу для телеграм бота, что бы сохранялась общая логика =(
class CurrencyApi:
    __DOMAIN__ = 'https://min-api.cryptocompare.com/data/'

    class ApiType(Enum):
        LIST_METHOD = 'blockchain/list'
        PRICE_METHOD = 'price'

    def __init__(self, api_key):
        self.__api_key = api_key

    def __build_url(self, method_type: ApiType, **params):
        params_str = ''
        for p in params:
            params_str += "{}={}&".format(p, params[p])
        return '{DOMAIN}{METHOD}?{PARAMS}api_key={API_KEY}'.format(
            DOMAIN=self.__DOMAIN__,
            METHOD=method_type.value,
            PARAMS=params_str,
            API_KEY=self.__api_key
        )

    def __make_request(self, method: ApiType, **params):
        url = self.__build_url(method, **params)
        return requests.get(url).json()

    def get_sys_list(self):
        r = self.__make_request(self.ApiType.LIST_METHOD)
        return [r['Data'][i]['symbol'] for i in r['Data']]

    def single_price(self, from_symbol, to_symbol):
        params = {
            'fsym': from_symbol,
            'tsyms': to_symbol
        }
        r = self.__make_request(self.ApiType.PRICE_METHOD, **params)
        try:
            return r[list(r.keys())[0]]
        except Exception as err:
            print(err)
            return None
