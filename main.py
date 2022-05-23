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

    scoreBase[update.message.from_user.username] = 0


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
    buttons = [KeyboardButton("Модуль 1"),
               KeyboardButton("Модуль 2"),
               KeyboardButton("Модуль 3"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)


def course3_moduls(update, context):
    buttons = [KeyboardButton("Модуль 1"),
               KeyboardButton("Модуль 2"),
               KeyboardButton("Модуль 3"),
               KeyboardButton("Нaзaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 3))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)

def hm_course(update, context):
    buttons = [KeyboardButton("Тест по теме \"Информационные системы в организации\""),
               KeyboardButton("Тест по теме \"Микроэкономика\""),
               KeyboardButton("Тест по теме \"Волновая физика\""),
               KeyboardButton("Назaд")]

    replyMarkup = ReplyKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Выберите, чем займемся сегодня",
                             reply_markup=replyMarkup)


# def answer(update, context):
#     query = update.callback_query
#     answ = query.data
#
#     query.answer()
#     query.delete_message()
#
#     if(answ == "right"):
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Правильно!")
#     else:
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Неправильно!")


def hm_course1_test(update, context):
    # answerHandler = CallbackQueryHandler(answer)
    buttons = [InlineKeyboardButton(text="Каскадная модель", callback_data='right'),
               InlineKeyboardButton(text="Модель параллельной разработки программных модулей", callback_data='wrong'),
               InlineKeyboardButton(text="Модель комплексного подхода к разработке ИС", callback_data='wrong'),
               InlineKeyboardButton(text="Объектно-ориентированная модель", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Наиболее распространённой моделью жизненного цикла является...",
                             reply_markup=replyMarkup)

    buttons = [InlineKeyboardButton(text="Закон убывающей доходности", callback_data='wrong'),
               InlineKeyboardButton(text="Закон циклического развития общества", callback_data='wrong'),
               InlineKeyboardButton(text="Закон “необходимого разнообразия", callback_data='right'),
               InlineKeyboardButton(text="Закон единства и борьбы противоположностей", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 2\nВ каком законе отображается объективность процесса информатизации общества?",
                             reply_markup=replyMarkup)

    buttons = [InlineKeyboardButton(text="Cообщения, находящиеся в памяти компьютера", callback_data='wrong'),
               InlineKeyboardButton(text="Cообщения, находящиеся в хранилищах данных", callback_data='wrong'),
               InlineKeyboardButton(text="Предварительно обработанные данные, годные для принятия управленческих решений", callback_data='right'),
               InlineKeyboardButton(text="Сообщения, зафиксированные на машинных носителях", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 3\nИнформация-это?",
                             reply_markup=replyMarkup)

def hm_course2_test(update, context):
    # answerHandler = CallbackQueryHandler(answer)
    buttons = [InlineKeyboardButton(text="Джоан Робинсон", callback_data='right'),
               InlineKeyboardButton(text="Адамом Смитом", callback_data='wrong'),
               InlineKeyboardButton(text="Джоном Кейнсом", callback_data='wrong'),
               InlineKeyboardButton(text="Альфредом Маршаллом", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Наиболее глубокий и полный анализ кардинально новых моментов несовершенной конкуренции был дан?",
                             reply_markup=replyMarkup)

    buttons = [InlineKeyboardButton(text="Минимальные средние издержки меньше, чем предельные издержки", callback_data='wrong'),
               InlineKeyboardButton(text="Цена меньше, чем минимальные средние переменные издержки", callback_data='right'),
               InlineKeyboardButton(text="Цена меньше, чем средние постоянные издержки", callback_data='wrong'),
               InlineKeyboardButton(text="Цена меньше, чем минимальные переменные издержки", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 2\nВ коротком периоде фирма с целью максимизировать прибыль или "
                                  "минимизировать убытки не должна производить товар, если:",
                             reply_markup=replyMarkup)

    buttons = [InlineKeyboardButton(text="Равновесие рынка труда нарушается из-за влияния профсоюзов", callback_data='wrong'),
               InlineKeyboardButton(text="Безработица характеризуется «естественным» уровнем", callback_data='wrong'),
               InlineKeyboardButton(text="Безработица препятствует нормальному функционированию рынка труда", callback_data='wrong'),
               InlineKeyboardButton(text="Безработица невозможна, если на рынке труда существует равновесие", callback_data='right')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 3\nПо мнению неоклассиков...",
                             reply_markup=replyMarkup)


def hm_course3_test(update, context):
    # answerHandler = CallbackQueryHandler(answer)
    buttons = [InlineKeyboardButton(text="Менее 20 Гц", callback_data='wrong'),
               InlineKeyboardButton(text="От 20 до 20 000 Гц", callback_data='wrong'),
               InlineKeyboardButton(text="Превышает 20 000 Гц", callback_data='right')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Ультразвуковыми называются колебания, частота которых ...",
                             reply_markup=replyMarkup)

    buttons = [InlineKeyboardButton(text="0,4 с", callback_data='right'),
               InlineKeyboardButton(text="0,2 с", callback_data='wrong'),
               InlineKeyboardButton(text="0,3 с", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 2\nЧерез какое время человек услышит эхо, если расстояние до преграды, "
                                  "отражающей звук, 68 м? Скорость звука в воздухе 340 м/с?",
                             reply_markup=replyMarkup)

    buttons = [InlineKeyboardButton(text="Радиоволны", callback_data='right'),
               InlineKeyboardButton(text="Инфракрасное излучение", callback_data='wrong'),
               InlineKeyboardButton(text="Видимое излучение", callback_data='wrong'),
               InlineKeyboardButton(text="Гамма-излучение", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 3\nСамая длинноволновая часть шкалы электромагнитных волн – ...",
                             reply_markup=replyMarkup)


def button(update, context):
    query = update.callback_query
    buttonValue = query.data


    query.answer()

    if(buttonValue == '1'):
        query.delete_message()
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
        query.delete_message()
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
        query.delete_message()
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
        query.delete_message()
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
        query.delete_message()
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

    elif (buttonValue == 'right'):
        if(query.from_user.username in scoreBase):
            scoreBase[query.from_user.username] += 10
            query.edit_message_text(text="Правильно!✅", reply_markup=None)
        else:
            query.edit_message_text(text="Вам нужно сначала зарегистрироваться, нажав /start", reply_markup=None)


    elif (buttonValue == 'wrong'):
        if (query.from_user.username in scoreBase):
            query.edit_message_text(text="Неправильно!❌", reply_markup=None)
        else:
            query.edit_message_text(text="Вам нужно сначала зарегистрироваться, нажав /start", reply_markup=None)


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


def statistic(update, context):
    text = "Вот наши лучшие пользователи👑:\n"
    top = []
    top = sorted(scoreBase, key=scoreBase.get)
    top.reverse()
    i = 1
    # print(str(top))
    for acc in top:
        text += str(i) + ". "
        text += str(acc) + "     " + str(scoreBase[acc])
        if(i == 1):
            text += "🥇"
        elif(i == 2):
            text += "🥈"
        elif (i == 3):
            text += "🥉"

        text += "\n"
        i += 1
        if(i > 10):
            break

    context.bot.send_message(chat_id=update.effective_chat.id, text=str(text))


if __name__ == '__main__':
    scoreBase = {}

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

    modul2Handler = MessageHandler(Filters.text("Курс 2"), course2_moduls)
    modul3Handler = MessageHandler(Filters.text("Курс 3"), course3_moduls)
    backkkHandler = MessageHandler(Filters.text("Нaзaд"), kurses)

    kurses1Handler = MessageHandler(Filters.text("Домашнее задание"), hm_course)
    modul11Handler = MessageHandler(Filters.text("Тест по теме \"Информационные системы в организации\""), hm_course1_test)
    modul22Handler = MessageHandler(Filters.text("Тест по теме \"Микроэкономика\""), hm_course2_test)
    modul33Handler = MessageHandler(Filters.text("Тест по теме \"Волновая физика\""), hm_course3_test)
    buttonHandler = CallbackQueryHandler(button)

    statisticHandler = MessageHandler(Filters.text("Статистика"), statistic)

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

    dispatcher.add_handler(modul2Handler)
    dispatcher.add_handler(modul3Handler)
    dispatcher.add_handler(backkkHandler)

    dispatcher.add_handler(kurses1Handler)
    dispatcher.add_handler(modul11Handler)
    dispatcher.add_handler(modul22Handler)
    dispatcher.add_handler(modul33Handler)

    dispatcher.add_handler(statisticHandler)

    dispatcher.add_handler(echoHandler)


    updater.start_polling()
