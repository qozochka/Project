import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    # создаем клавиатуру
    input_data_keyboard_1 = types.InlineKeyboardMarkup()

    # добавляем на нее кнопки
    button_rent = types.InlineKeyboardButton("Снять", callback_data="rent")
    button_buy = types.InlineKeyboardButton("Купить", callback_data="buy")
    input_data_keyboard_1.add(button_rent)
    input_data_keyboard_1.add(button_buy)

    bot.send_message(message.chat.id, "Давайте подберем вам квартиру, только ответь на пару вопросов.")
    bot.send_message(message.chat.id, "Вы хотить снять или купить квартиру?", reply_markup=input_data_keyboard_1)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "rent":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "Хорошо")
        if call.data == "":
            bot.send_message(call.message.chat.id, "Иди деньги сначала заработай ботик")


bot.infinity_polling()
