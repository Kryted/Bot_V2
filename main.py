import telebot
from telebot import types

bot = telebot.TeleBot('6915080004:AAEGt2HW3RlVyviTk9GtxL6mvncixQ1VyxQ')


@bot.message_handler(commands=['start'])
def main(messadge):
   bot.send_message(messadge.chat.id, messadge)



bot.polling(none_stop=True)    #код для постоянной работы бота