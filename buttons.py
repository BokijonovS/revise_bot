from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = KeyboardButton('Shahar nomi boyicha 🏙')
    btn2 = KeyboardButton('Lokatsiya boyicha 🗺️', request_location=True)
    markup.add(btn1, btn2)
    return markup
