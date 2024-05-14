import telebot
from telebot import types

bot = telebot.TeleBot('6915080004:AAEGt2HW3RlVyviTk9GtxL6mvncixQ1VyxQ')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('запустить функцию')
    btn3 = types.KeyboardButton('запустить функцию_2')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, "привет", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'перейти на сайт':
        bot.send_message(message.chat.id, 'перешел')
    elif message.text == 'запустить функцию':
        bot.send_message(message.chat.id, 'запустил')



bot.polling(none_stop=True)    #код для постоянной работы бота