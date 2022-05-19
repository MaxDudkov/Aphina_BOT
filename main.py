from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import Updater

TOKEN = '5290614906:AAGYFaOjyqukQHJDwBiLfpHih-xSmS0smx4'


def menuBuilder(buttons, n_cols, headerButtons=None, footerButtons=None):
    menu = [buttons[i: i + n_cols] for i in range(0, len(buttons), n_cols)]

    if(headerButtons):
        menu.insert(0, [headerButtons])

    if(footerButtons):
        menu.append([footerButtons])

    return menu


def echo(update, context):

    if update.message:
        if update.message.text:
            update.message.reply_text(f'Я пока не знаю, что на это ответить :(')


def start(update, context):
    buttons = [KeyboardButton("О нас"),
               KeyboardButton("Контакты"),
               KeyboardButton("Услуги")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Приветственное сообщение",
                             reply_markup=replyMarkup)


def services(update, context):
    buttons = [KeyboardButton("Курсы"),
               KeyboardButton("Домашнее задание"),
               KeyboardButton("Статистика"),
               KeyboardButton("Мини-Игры"),
               KeyboardButton("Назад")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 4))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)


def button(update, _):
    query = update.callback_query
    buttonValue = query.data

    query.answer()
    query.edit_message_text(text=f"Выбранный вариант: {buttonValue}")

def about(update, context):
    replyMarkup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Назад")], 1))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Наши решения", reply_markup=replyMarkup)


def contact(update, context):
    replyMarkup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Назад")], 1))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Контакты", reply_markup=replyMarkup)


if __name__ == '__main__':
    global UPDATE_ID
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    startHandler = CommandHandler('start', start)
    aboutHandler = MessageHandler(Filters.text("О нас"), about)
    contactHandler = MessageHandler(Filters.text("Контакты"), contact)
    serviceHandler = MessageHandler(Filters.text("Услуги"), services)
    backHandler = MessageHandler(Filters.text("Назад"), start)
    buttonHandler = CallbackQueryHandler(button)

    echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(startHandler)
    dispatcher.add_handler(aboutHandler)
    dispatcher.add_handler(contactHandler)
    dispatcher.add_handler(serviceHandler)
    dispatcher.add_handler(backHandler)
    dispatcher.add_handler(buttonHandler)
    dispatcher.add_handler(echoHandler)


    updater.start_polling()
