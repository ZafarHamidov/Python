import telebot
from time import sleep
import random

TOKEN = "1652721367:AAH31eI71XLybHEyG4g-Y-hAT-c-j8Uq-as"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["dom"])
@bot.message_handler(commands=["рандом"])
def random_num(message):
    num = random.randint(0, 1000)
    bot.send_message(message.chat.id, str(num))

@bot.message_handler(commands=["СТАРТ"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я бот помощник")

@bot.message_handler(content_types=["text"])
def text(message):
    if message.text.lower() == "салам":
        bot.send_message(message.chat.id, "салам алейкум")


bot.polling()
