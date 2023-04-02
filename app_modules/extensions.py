from app_modules.currency_module.currence_api import single_price, get_sys_list


class CryptoCurrency:

    @staticmethod
    def get_price(base, quote, amount):
        value = float(single_price(base, quote))
        if value:
            result = value * amount
            return quote + " : " + str(result)
        return

    @staticmethod
    def currency_list():
        return get_sys_list()