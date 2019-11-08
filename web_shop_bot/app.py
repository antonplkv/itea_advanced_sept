import telebot
from telebot.types import (
InlineKeyboardMarkup,
InlineKeyboardButton
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


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['products'])
def show_categories(message):
    """
    :param message:
    :return: listed root categories
    """
    category_queryset = models.Category.get_root_categories()
    kb = keyboards.InlineKB(
        iterable=category_queryset,
        lookup_field='id',
        named_arg='category',
    )

    bot.send_message(message.chat.id, "Выберите категорию", reply_markup=kb.generate_kb())


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_products_or_sub_category(call):
    """

    :param call:
    :return: listed subcategories || listed products
    """
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()
    if category.is_parent:
        kb = keyboards.InlineKB(
            iterable=category.subcategory,
            lookup_field='id',
            named_arg='category'
        )

        bot.edit_message_text(text=category.title,chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=kb.generate_kb())
       # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.generate_kb())


    else:
        print("NON PARENT")



if __name__ == '__main__':

    bot.polling(none_stop=True)
