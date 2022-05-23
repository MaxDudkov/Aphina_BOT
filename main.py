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


def firstStart(update, context):
    buttons = [KeyboardButton("О нас"),
               KeyboardButton("Контакты"),
               KeyboardButton("Услуги")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет, " + update.message.from_user.first_name + ", меня зовут Афина!☺\n"
                                  "Я твой путеводитель в мир образования. "
                                  "Уверена что мы с тобой сработаемся и достигнем множества вершин. "
                                  "Мне не терпится показать тебе что я могу. Давай же начнём!🥳",
                             reply_markup=replyMarkup)


def start(update, context):
    buttons = [KeyboardButton("О нас"),
               KeyboardButton("Контакты"),
               KeyboardButton("Услуги")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Чем займёмся теперь ?",
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


def kurses(update, context):
    buttons = [KeyboardButton("Информационные системы в организации"),
               KeyboardButton("Курс 2"),
               KeyboardButton("Курс 3"),
               KeyboardButton("Назaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите курс, который хотите пройти",
                             reply_markup=replyMarkup)


def course1_moduls(update, context):
    buttons = [KeyboardButton("Информация и информационные технологии"),
               KeyboardButton("Правовые информационные системы"),
               KeyboardButton("Информационные технологии и структура управления"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)

def course_1_modul_1(update, context):
    filename = open('./courses/course1_1.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course_1_modul_2(update, context):
    filename = open('./courses/course1_2.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course_1_modul_3(update, context):
    filename = open('./courses/course1_3.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course2_moduls(update, context):
    buttons = [KeyboardButton("Введение в микроэкономику"),
               KeyboardButton("ПРЕДПРИЯТИЕ (ФИРМА)"),
               KeyboardButton("Издержки и доходы предприятия"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)

def course_2_modul_1(update, context):
    filename = open('./courses/course2_1.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course_2_modul_2(update, context):
    filename = open('./courses/course2_2.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course_2_modul_3(update, context):
    filename = open('./courses/course2_3.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course3_moduls(update, context):
    buttons = [KeyboardButton("Упругие волны скорость энергия"),
               KeyboardButton("Стоячая волна эффект Доплера"),
               KeyboardButton("Электромагнитные волны световая волна"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)

def course_3_modul_1(update, context):
    filename = open('./courses/course3_1.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course_3_modul_2(update, context):
    filename = open('./courses/course3_2.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)


def course_3_modul_3(update, context):
    filename = open('./courses/course3_3.pdf', 'rb')
    context.bot.send_document(update.effective_chat.id, filename)

def hm_course(update, context):
    buttons = [KeyboardButton("Курc 1"),
               KeyboardButton("Курc 2"),
               KeyboardButton("Курc 3"),
               KeyboardButton("Назaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)


def hm_course1_moduls(update, context):
    buttons = [KeyboardButton("Модуль 1"),
               KeyboardButton("Модуль 2"),
               KeyboardButton("Модуль 3"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)

def hm_course2_moduls(update, context):
    buttons = [KeyboardButton("Модуль 1"),
               KeyboardButton("Модуль 2"),
               KeyboardButton("Модуль 3"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)

def hm_course3_moduls(update, context):
    buttons = [KeyboardButton("Модуль 1"),
               KeyboardButton("Модуль 2"),
               KeyboardButton("Модуль 3"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
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
    buttons = [InlineKeyboardButton("Мы Вконтакте💙", url="https://vk.com/cg_rus"),
               InlineKeyboardButton("Мы в YouTube❤", url="https://www.youtube.com/channel/UC22mNxwdy5YgIObb-l-pfWw"),
               InlineKeyboardButton("Мы в Telegram💜", url="https://t.me/edutainment_com")]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Наши контакты!\n\n"
                                                                    "Офис в Москве:\n129343, проезд Серебрякова, 14с15,"
                                                                    "БЦ «Сильвер Стоун»."
                                                                    "\nEmail:\nletsplay@center-game.com"
                                                                    "\nТелефон:\n+7 985 338 32 93", reply_markup=replyMarkup)

    context.bot.send_message(chat_id=update.effective_chat.id, text="Представительство в Узбекистане:\n\n"
                                                                    "Адрес: 100052, г. Ташкент, ул. Кургон, 3-й проезд, д.3"
                                                                    "\nEmail: \nlev.gavrish@gmail.com"
                                                                    "\nWeb: \nwww.change.uz"
                                                                    "\nТелефон: \n+998 (93) 555 0210")


if __name__ == '__main__':
    global UPDATE_ID
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    startHandler = CommandHandler('start', firstStart)

    aboutHandler = MessageHandler(Filters.text("О нас"), about)
    contactHandler = MessageHandler(Filters.text("Контакты"), contact)
    serviceHandler = MessageHandler(Filters.text("Услуги"), services)
    backHandler = MessageHandler(Filters.text("Назад"), start)

    kursesHandler = MessageHandler(Filters.text("Курсы"), kurses)
    backkHandler = MessageHandler(Filters.text("Назaд"), services)

    modul1Handler = MessageHandler(Filters.text("Информационные системы в организации"), course1_moduls)
    course_1_1_Handler = MessageHandler(Filters.text("Информация и информационные технологии"), course_1_modul_1)
    course_1_2_Handler = MessageHandler(Filters.text("Правовые информационные системы"), course_1_modul_2)
    course_1_3_Handler = MessageHandler(Filters.text("Информационные технологии и структура управления"), course_1_modul_3)

    modul2Handler = MessageHandler(Filters.text("Микроэкономика"), course2_moduls)
    course_2_1_Handler = MessageHandler(Filters.text("Введение в микроэкономику"), course_2_modul_1)
    course_2_2_Handler = MessageHandler(Filters.text("ПРЕДПРИЯТИЕ (ФИРМА)"), course_2_modul_2)
    course_2_3_Handler = MessageHandler(Filters.text("Издержки и доходы предприятия"), course_2_modul_3)

    modul3Handler = MessageHandler(Filters.text("Волновая физика"), course3_moduls)
    course_3_1_Handler = MessageHandler(Filters.text("Упругие волны скорость энергия"), course_3_modul_1)
    course_3_2_Handler = MessageHandler(Filters.text("Стоячая волна эффект Доплера"), course_3_modul_2)
    course_3_3_Handler = MessageHandler(Filters.text("Электромагнитные волны световая волна"), course_3_modul_3)

    backkkHandler = MessageHandler(Filters.text("Нaзaд"), kurses)

    kurses1Handler = MessageHandler(Filters.text("Домашнее задание"), hm_course)
    modul11Handler = MessageHandler(Filters.text("Курc 1"), hm_course1_moduls)
    modul22Handler = MessageHandler(Filters.text("Курc 2"), hm_course2_moduls)
    modul33Handler = MessageHandler(Filters.text("Курc 3"), hm_course3_moduls)
    buttonHandler = CallbackQueryHandler(button)

    echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)

    dispatcher.add_handler(startHandler)
    dispatcher.add_handler(aboutHandler)
    dispatcher.add_handler(contactHandler)
    dispatcher.add_handler(serviceHandler)
    dispatcher.add_handler(backHandler)
    dispatcher.add_handler(buttonHandler)

    dispatcher.add_handler(kursesHandler)
    dispatcher.add_handler(backkHandler)

    dispatcher.add_handler(modul1Handler)
    dispatcher.add_handler(course_1_1_Handler)
    dispatcher.add_handler(course_1_2_Handler)
    dispatcher.add_handler(course_1_3_Handler)

    dispatcher.add_handler(course_2_1_Handler)
    dispatcher.add_handler(course_2_2_Handler)
    dispatcher.add_handler(course_2_3_Handler)

    dispatcher.add_handler(course_3_1_Handler)
    dispatcher.add_handler(course_3_2_Handler)
    dispatcher.add_handler(course_3_3_Handler)

    dispatcher.add_handler(modul2Handler)
    dispatcher.add_handler(modul3Handler)
    dispatcher.add_handler(backkkHandler)

    dispatcher.add_handler(kurses1Handler)
    dispatcher.add_handler(modul11Handler)
    dispatcher.add_handler(modul22Handler)
    dispatcher.add_handler(modul33Handler)
    dispatcher.add_handler(echoHandler)


    updater.start_polling()
