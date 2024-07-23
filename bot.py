from pprint import pprint

import requests
import telebot
from telebot.types import Message


API_TOKEN = '7377852260:AAGWBFA5t53iS7Cu0_TQBKgwcr57hZMBw8E'
city_name = 'Fergana'
api_key = '3b502459ad3dac3cb3eeb8d9637e5e07'

parameters = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric'
}

api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?", params=parameters).json()
pprint(api['main']['temp'])

bot = telebot.TeleBot(API_TOKEN, parse_mode='html')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alekum {message.from_user.first_name}\n"
                              f"<b>Ob havo</b> botiga xush kelibsiz!")




if __name__ == '__main__':
    bot.infinity_polling()
