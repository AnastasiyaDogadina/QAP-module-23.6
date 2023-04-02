import telebot
import os
from app_modules.extensions import CryptoCurrency
from app_modules.telegram_module import text_messages

bot = telebot.TeleBot(os.getenv("TG_TOKEN"))


@bot.message_handler(commands=['values'])
def handle_start_help(message):
    list_sys = CryptoCurrency.currency_list()
    response_message = ''
    for sys in list_sys:
        response_message += sys + '\n'
        if len(response_message) > 200:
            bot.reply_to(message, response_message)
            response_message = ''


@bot.message_handler(commands=['start', 'help'])
def handle_values(message):
    bot.reply_to(message, text_messages.HELLO_TEXT)


@bot.message_handler()
def message_handle_currency(message):
    input_message = message.json['text']
    text_as_arr = input_message.split(' ')

    if len(text_as_arr) != 3:
        bot.reply_to(message, text_messages.WRONG_COMMAND)
        return
    try:
        amount = float(text_as_arr[2])
    except ValueError:
        bot.reply_to(message, text_messages.WRONG_FLOAT_VALUE)
        return

    list_sys = CryptoCurrency.currency_list()
    for input_currency in text_as_arr[0:2]:
        if input_currency.upper() not in list_sys:
            bot.reply_to(message, text_messages.CURRENCY_NOT_FOUND.format(input_currency))
            return
    result = CryptoCurrency.get_price(text_as_arr[0], text_as_arr[1], amount)
    bot.reply_to(message, result if result else text_messages.SOME_CONVERT_ERROR)


def start_bot():
    bot.polling(none_stop=True)
