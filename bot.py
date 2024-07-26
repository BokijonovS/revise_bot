from pprint import pprint
from datetime import datetime
import requests
import telebot
from telebot.types import Message, ReplyKeyboardRemove
from buttons import main_menu


API_TOKEN = '7377852260:AAGWBFA5t53iS7Cu0_TQBKgwcr57hZMBw8E'
api_key = '3b502459ad3dac3cb3eeb8d9637e5e07'

parameters = {
    'appid': api_key,
    'units': 'metric'
}


bot = telebot.TeleBot(API_TOKEN, parse_mode='html')


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alekum {message.from_user.first_name}\n"
                              f"<b>Ob havo</b> botiga xush kelibsiz!", reply_markup=main_menu())


@bot.message_handler(regexp="Shahar nomi boyicha 🏙")
def text(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Shahar nomini kiriting!", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_city_name)


def get_city_name(message: Message):
    chat_id = message.chat.id
    parameters['q'] = message.text
    api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?", params=parameters).json()
    pprint(api)
    name = api['name']
    desc = api['weather'][0]['description']
    temp = api['main']['temp']
    humidity = api['main']['humidity']
    sunrise = datetime.fromtimestamp(api['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(api['sys']['sunset']).strftime('%H:%M')
    wind = api['wind']['speed']
    info = (f"{name} shahrida ob havo: {desc}\n"
            f"Havo harorati: {temp} C°\n"
            f"Namlik: {humidity}%\n"
            f"Quyosh chiqishi: {sunrise}\n"
            f"Quyosh botishi: {sunset}\n"
            f"Shamol tezligi: {wind}m/s")
    bot.send_message(chat_id, info, reply_markup=main_menu())


@bot.message_handler(content_types=['location'])
def get_location(message: Message):
    chat_id = message.chat.id
    params = {
        'appid': api_key,
        'lat': message.location.latitude,
        'lon': message.location.longitude,
        'units': 'metric'
    }
    api = requests.get(f"https://api.openweathermap.org/data/2.5/weather?", params=params).json()
    name = api['name']
    desc = api['weather'][0]['description']
    temp = api['main']['temp']
    humidity = api['main']['humidity']
    sunrise = datetime.fromtimestamp(api['sys']['sunrise']).strftime('%H:%M')
    sunset = datetime.fromtimestamp(api['sys']['sunset']).strftime('%H:%M')
    wind = api['wind']['speed']
    info = (f"{name} shahrida ob havo: {desc}\n"
            f"Havo harorati: {temp} C°\n"
            f"Namlik: {humidity}%\n"
            f"Quyosh chiqishi: {sunrise}\n"
            f"Quyosh botishi: {sunset}\n"
            f"Shamol tezligi: {wind}m/s")
    bot.send_message(chat_id, info, reply_markup=main_menu())


if __name__ == '__main__':
    bot.infinity_polling()
