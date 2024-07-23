from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    markup = ReplyKeyboardMarkup()
    btn1 = KeyboardButton('Ob havo')
    btn2 = KeyboardButton('Info')
    markup.add(btn1, btn2)
    return markup
