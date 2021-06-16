from telebot import types
import config
import emoji


bot = config.link


@bot.callback_query_handler(func=lambda call: call.data in ['start_order', 'help'])
def callback_inline(call):
    try:
        if call.message:
            if call.data == "start_order":
                bot.send_message(call.message.chat.id, "Ну начнем")
                if bot.answer_inline_query("Перейти к сбору заказа"):
                    bot.send_message(call.message.chat.id, "Привет")
            if call.data == "help":
                help_mess(call.message)

    except Exception as e:
        print(repr(e))


def help_mess(message):
    reply_markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Связаться с поддержкой")
    btn2 = types.KeyboardButton("Назад")
    reply_markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "ЕСЛИ бот работает НЕКОРРЕКТНО\n"
                                      "Вы можете оставить сообщение поддержке,\n"
                                      "И с вами свяжуться через некоторое время.",
                     reply_markup=reply_markup)


@bot.message_handler(content_types=["text"])
def main_logic(message):
    def start(mess, mess_bot):
        reply_markup = types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton("Перейти к сбору заказа", callback_data="start_order")],
            [types.InlineKeyboardButton("Нужна помощь", callback_data="help")]
        ])

        bot.send_message(mess.chat.id, mess_bot, reply_markup=reply_markup)

    if message.text == "/start" or str(message.text).casefold() == "привет":
        message_bot = f"Привет {message.from_user.first_name}!\nЯ бот kaMata0 \U0001F47D\nИ я помогу тебе с покупками."
        start(message, message_bot)

    elif message.text == "Назад":
        message_bot = "Окей вернемся в самое начало"
        start(message, message_bot)

    elif str(message.text).casefold() == "cвязаться с поддержкой":
        bot.send_message(message.chat.id, f"")


    else:
        bot.reply_to(message, "Я вас не понимаю")


if __name__ == '__main__':
    bot.polling(none_stop=True)
