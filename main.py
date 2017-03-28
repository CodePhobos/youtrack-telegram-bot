import logging

import telebot

import cfg


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(cfg.app.bot_token)


@bot.message_handler(commands=["start"])
def welcome_message(message):
    bot.reply_to(message, "Yo")


@bot.message_handler(func=lambda message: message.text == "yo")
def answer(message):
    bot.reply_to(message, "you said password, come in")


@bot.message_handler(content_types=["audio"])
def audio(message):
    print(message)


bot.polling()
