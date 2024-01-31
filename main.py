import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN_HERE")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling()
