import telebot
from telebot.types import Message

API_TOKEN = '7377852260:AAGWBFA5t53iS7Cu0_TQBKgwcr57hZMBw8E'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alekum {message.from_user.first_name}")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()