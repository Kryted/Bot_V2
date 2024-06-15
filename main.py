from src.functions import reading_employee, write_employee, add_new_employee, delete_old_employee, search_employee_data
import telebot
from telebot import types

bot = telebot.TeleBot('6915080004:AAEGt2HW3RlVyviTk9GtxL6mvncixQ1VyxQ')


@bot.message_handler(commands=['start'])
def main(messadge):
   bot.send_message(messadge.chat.id, messadge)



bot.polling(none_stop=True)    #код для постоянной работы бота