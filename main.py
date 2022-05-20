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


def button(update, context):
    query = update.callback_query
    buttonValue = query.data


    query.answer()
    query.delete_message()

    if(buttonValue == '1'):
        img = open('./img/about_1_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Кейс \"СберУниверситет\"", url="https://center-game.com/leaderclub")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Кейс НПФ \"Эволюция\"", url="https://center-game.com/npfevolution")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1_3.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Кейс М.Видео-Эльдорадо под ключ", url="https://center-game.com/mvideoacademy")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1_4.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Кейс Лидер-клуба СберУниверсита", url="https://center-game.com/case_leaderclub2")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1_5.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Центр управления мотивацие для 2,5 тысяч трейдеров", url="https://center-game.com/traders")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1_6.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Центр управления мотивацией для марафона от «Преактум»",
                                  url="https://center-game.com/preactum")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1_7.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Центр управления мотивацией для «Техавтоцентра»",
                                  url="https://center-game.com/tac")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

    elif(buttonValue == '2'):
        img = open('./img/about_2_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Онлайн-лекторий юбилейного Фестиваля науки NAUKA", url="https://center-game.com/naukafest")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_2_2.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Как превратить IT-конференцию в роман Нила Геймана — на примере Ростелекома", url="https://center-game.com/rtk_friday13")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_2_3.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Платформа для онлайн-форума АНО «Россия — страна возможностей»", url="https://center-game.com/zavtraforum")],
            1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_2_4.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Онлайн-платформа конференции «АРТtalk»",
                                  url="https://center-game.com/arttalk")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_2_5.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Первая конференция о социальном спорте для Благотворительного фонда Владимира Потанина",
                                  url="https://center-game.com/potanin_conf")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_2_6.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Платформа онлайн-форума iВолга для Самарской области",
                                  url="https://center-game.com/ivolga")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_2_7.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Как удержать внимание на 6-часовой онлайн-конференции",
                                  url="https://center-game.com/edfest")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

    elif (buttonValue == '3'):
        img = open('./img/about_3_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Интерактивный Атлас профессий Сбера и НИУ ВШЭ",
                                  url="https://center-game.com/sber_atlas")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_3_2.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Как объяснить работу эндаумент-фонда через настольную игру — в кейсе эндаумента МФТИ",
                                  url="https://center-game.com/mipt_endowment")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_3_3.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="17 видеоуроков о личной миссии «Путь самурая» для российского ESET",
                                  url="https://center-game.com/esetsamurai")],
            1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_3_4.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Как сделать профориентацию интересной для школьников — в кейсе «Билета в Будущее»",
                                  url="https://center-game.com/biletvbuduschee")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_3_5.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(
                text="Игра «Лабиринт» для введения в ТРИЗ",
                url="https://center-game.com/labirint")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_3_6.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Интерактивный квиз о защите данных",
                                  url="https://center-game.com/bernache")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

    elif (buttonValue == '4'):
        img = open('./img/about_4_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Оценка 360°, которая меняет корпоративную культуру в ESET",
                                  url="https://center-game.com/eset")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_4_2.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Развитие навыков работы c клиентами у инженеров DataLine",
                                  url="https://center-game.com/dataline ")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_4_3.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Новая схема коммуникаций для операционного департамента Faberlic",
                                  url="https://center-game.com/faberlic")],
            1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_4_4.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Курс по управлению людьми, проектами и собой для МИСиС",
                                  url="https://center-game.com/misis")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

    elif (buttonValue == '5'):
        img = open('./img/about_5_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Интерактивный зал в историческом парке на ВДНХ",
                                  url="https://center-game.com/histpark")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_3_1.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Интерактивный Атлас профессий Сбера и НИУ ВШЭ",
                                  url="https://center-game.com/sber_atlas")], 1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)

        img = open('./img/about_1_3.jpg', 'rb')
        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
            [InlineKeyboardButton(text="Кейс М.Видео-Эльдорадо под ключ", url="https://center-game.com/mvideoacademy")],
            1))
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)


def about(update, context):
    buttons = [InlineKeyboardButton("Дистанционное обучение", callback_data='1'),
               InlineKeyboardButton("Онлайн-мероприятия", callback_data='2'),
               InlineKeyboardButton("Новые формы обучения", callback_data='3'),
               InlineKeyboardButton("Консалтинг в обучении", callback_data='4'),
               InlineKeyboardButton("Комплексные проекты", callback_data='5')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вот наши решения!",
                             reply_markup=replyMarkup)



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
