import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,
)
import config
import keyboards
from models import models
from keyboards import ReplyKB
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    #greetings_str = models.Texts(title='Greetings').get().body
    greeting_str = 'Hi'

    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)



if __name__ == '__main__':
    bot.polling(none_stop=True)
