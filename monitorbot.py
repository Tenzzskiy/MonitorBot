from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;
import telebot
from telebot import types #maxim bog

TG_TOKEN = "1249821761:AAFY_IpiaIvvX-XWGl_eFyCuz6UeW-dL76Y"

bot = telebot.TeleBot("1249821761:AAFY_IpiaIvvX-XWGl_eFyCuz6UeW-dL76Y")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="Страница моего создателя в ВК", url="https://vk.com/psychocave")
    nextpage_button = types.InlineKeyboardButton(text="Перейти на следующую страницу", callback_data="next")
    shops_button = types.InlineKeyboardButton(text="Список доступных магазинов", callback_data="shops")
    keyboard.add(shops_button, nextpage_button, url_button)
    bot.send_message(message.chat.id,
                     "Добро пожаловать!👋 \nЯ Бот Монитор, ниже представлены команды, которые я могу выполнять 🤖",
                     reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def handle_start_text(message):
    if message.text == "Максон":
        bot.send_message(message.chat.id, "Да\nДа Да\nЭт я)")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton(text="Страница моего создателя в ВК", url="https://vk.com/psychocave")
    nextpage_button = types.InlineKeyboardButton(text="Перейти на следующую страницу", callback_data="next")
    shops_button = types.InlineKeyboardButton(text="Список доступных магазинов", callback_data="shops")
    keyboard.add(shops_button, nextpage_button, url_button)
    bot.send_message(message.chat.id,
                     "Добро пожаловать!👋 \nЯ Бот Монитор, ниже представлены команды, которые я могу выполнять 🤖",
                     reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "shops":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton(text="Вернуться назад", callback_data="back")
        keyboard.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="❓ Ниже представлен список магазинов из которых будут представлены цены ❓", reply_markup=keyboard)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Магазины")
    elif call.data == "back":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button = types.InlineKeyboardButton(text="Страница моего создателя в ВК", url="https://vk.com/psychocave")
        nextpage_button = types.InlineKeyboardButton(text="Перейти на следующую страницу", callback_data="next")
        faq_button = types.InlineKeyboardButton(text="Часто задаваемые вопросы (FAQ)", callback_data="faq")
        keyboard.add(shops_button, nextpage_button, url_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                     text="Добро пожаловать!👋 \nЯ Бот Монитор, ниже представлены команды, которые я могу выполнять 🤖",
                              reply_markup=keyboard)



if __name__ == '__main__':
    bot.infinity_polling()
