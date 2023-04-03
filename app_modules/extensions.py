from app_modules.currency_module.currence_api import CurrencyApi
import os


class CryptoCurrency:
    __API = CurrencyApi(api_key=os.getenv('CRYPTO_API_KEY'))

    @staticmethod
    def get_price(base, quote, amount):
        value = float(CryptoCurrency.__API.single_price(base, quote))
        if value:
            result = value * amount
            return quote + " : " + str(result)
        return

    @staticmethod
    def currency_list():
        return CryptoCurrency.__API.get_sys_list()
