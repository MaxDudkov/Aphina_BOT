import logging
from time import sleep

import telegram
from telegram.error import NetworkError, Unauthorized
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import Updater

TOKEN = '5290614906:AAGYFaOjyqukQHJDwBiLfpHih-xSmS0smx4'


def echo(update, context):

    if update.message:
        if update.message.text:
            update.message.reply_text(f'Я пока не знаю, что на это ответить :(')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="start text")


if __name__ == '__main__':
    global UPDATE_ID
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    startHandler = CommandHandler('start', start);
    echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(startHandler)
    dispatcher.add_handler(echoHandler)


    updater.start_polling()
