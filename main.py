from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import Updater
import yaml
import logging

TOKEN = '5290614906:AAGYFaOjyqukQHJDwBiLfpHih-xSmS0smx4'


class App(object):
    def __init__(self, token):
        self.config = None
        self.token = token
        self.score_base = {}
        self.last_command = {}
        logging.basicConfig(level=logging.DEBUG)

    def run(self):
        updater = Updater(token=self.token, use_context=True)
        dispatcher = updater.dispatcher

        self.config = yaml.safe_load(open('config.yml'))

        for cmd in self.config['commands']:
            match cmd['type']:

                case 'interactive_command':
                    handler = CommandHandler(cmd['cmd'], self.make_cmd(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added /command %s", cmd['name'])

                case 'file':
                    handler = MessageHandler(Filters.text(cmd['cmd']), self.make_file_cb(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added file command %s", cmd['name'])

                case 'default_message':
                    handler = MessageHandler(Filters.text(cmd['cmd']), self.make_cb(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added command %s", cmd['name'])

                case 'back_button':
                    handler = MessageHandler(Filters.text(cmd['cmd']), self.make_back_button(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added back command")

        buttonHandler = CallbackQueryHandler(self.button)
        echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)

        dispatcher.add_handler(buttonHandler)
        dispatcher.add_handler(echoHandler)

        updater.start_polling()

    def make_cb(self, cmd):
        if cmd.get('callback_data', False):
            if (cmd.get('url', False)):
                replyMarkup = InlineKeyboardMarkup(
                    menuBuilder([InlineKeyboardButton(x, url=str(i)) for i, x in
                                 zip(cmd['callback_data'], cmd['buttons'])], cmd['buttons_count']))
            else:
                replyMarkup = InlineKeyboardMarkup(
                    menuBuilder([InlineKeyboardButton(x, callback_data=str(i)) for i, x in
                        zip(cmd['callback_data'], cmd['buttons'])], cmd['buttons_count']))
        else:
            replyMarkup = ReplyKeyboardMarkup(
                menuBuilder([KeyboardButton(x) for x in cmd['buttons']], cmd['buttons_count']))

        def callback_func(upd, ctx):
            self.last_command[upd.message.from_user.username] = cmd['name']
            logging.info('user %s cmd %s', upd.message.from_user.username, cmd['name'])
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=cmd['text'], reply_markup=replyMarkup)

        return callback_func

    def make_file_cb(self, cmd):
        def callback_func(upd, ctx):
            logging.info('user %s cmd %s', upd.message.from_user.username, cmd['name'])
            filename = open(cmd['file'], 'rb')
            ctx.bot.send_document(upd.effective_chat.id, filename)

        return callback_func

    def make_cmd(self, cmd):
        if cmd.get('callback_data', False):
            if (cmd.get('url', False)):
                replyMarkup = InlineKeyboardMarkup(
                    menuBuilder([InlineKeyboardButton(x, url=str(i)) for i, x in
                                 zip(cmd['callback_data'], cmd['buttons'])], cmd['buttons_count']))
            else:
                replyMarkup = InlineKeyboardMarkup(
                    menuBuilder([InlineKeyboardButton(x, callback_data=str(i)) for i, x in
                        zip(cmd['callback_data'], cmd['buttons'])], cmd['buttons_count']))
        else:
            replyMarkup = ReplyKeyboardMarkup(
                menuBuilder([KeyboardButton(x) for x in cmd['buttons']], cmd['buttons_count']))

        def callback_funk(upd, ctx):
            text = cmd['text'].format(msg=upd.message)
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=text, reply_markup=replyMarkup)

        return callback_funk

    def make_back_button(self, cmd):
        def callback_funk(upd, ctx):
            last_menu = {}
            for c in self.config['commands']:
                if c['name'] == self.last_command[upd.message.from_user.username]:
                    last_screen_name = c['prev_screen']
                    break

            for c in self.config['commands']:
                if c['name'] == last_screen_name:
                    last_menu = c
                    break

            self.last_command[upd.message.from_user.username] = last_screen_name
            replyMarkup = ReplyKeyboardMarkup(
                menuBuilder([KeyboardButton(x) for x in last_menu['buttons']], last_menu['buttons_count']))

            text = last_menu['text'].format(msg=upd.message)
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=text, reply_markup=replyMarkup)

        return callback_funk

    def user_init(self, username):
        if username not in self.score_base.keys():
            self.score_base[username] = 0

    def button(self, update, context):
        query = update.callback_query
        buttonValue = query.data

        query.answer()

        for btn in self.config['buttons']:
            if btn['button_value'] == buttonValue:
                match btn['type']:
                    case 'ads':
                        query.delete_message()
                        for msg in btn['messages']:
                            img = open(msg['img'], 'rb')
                            inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
                                [InlineKeyboardButton(text=msg['text'],
                                                      url=msg['url'])], 1))
                            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img,
                                                   reply_markup=inlineReplyMarkup)

                    case 'test_wrong':
                        query.edit_message_text(text=msg['text'], reply_markup=None)

                    case 'test_right':
                        query.edit_message_text(text=msg['text'], reply_markup=None)


        #
        # elif (buttonValue == '3'):
        #     query.delete_message()
        #     img = open('./img/about_3_1.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Интерактивный Атлас профессий Сбера и НИУ ВШЭ",
        #                               url="https://center-game.com/sber_atlas")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_3_2.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(
        #             text="Как объяснить работу эндаумент-фонда через настольную игру — в кейсе эндаумента МФТИ",
        #             url="https://center-game.com/mipt_endowment")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_3_3.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="17 видеоуроков о личной миссии «Путь самурая» для российского ESET",
        #                               url="https://center-game.com/esetsamurai")],
        #         1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_3_4.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(
        #             text="Как сделать профориентацию интересной для школьников — в кейсе «Билета в Будущее»",
        #             url="https://center-game.com/biletvbuduschee")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_3_5.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(
        #             text="Игра «Лабиринт» для введения в ТРИЗ",
        #             url="https://center-game.com/labirint")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_3_6.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Интерактивный квиз о защите данных",
        #                               url="https://center-game.com/bernache")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        # elif (buttonValue == '4'):
        #     query.delete_message()
        #     img = open('./img/about_4_1.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Оценка 360°, которая меняет корпоративную культуру в ESET",
        #                               url="https://center-game.com/eset")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_4_2.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Развитие навыков работы c клиентами у инженеров DataLine",
        #                               url="https://center-game.com/dataline ")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_4_3.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Новая схема коммуникаций для операционного департамента Faberlic",
        #                               url="https://center-game.com/faberlic")],
        #         1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_4_4.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Курс по управлению людьми, проектами и собой для МИСиС",
        #                               url="https://center-game.com/misis")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        # elif (buttonValue == '5'):
        #     query.delete_message()
        #     img = open('./img/about_5_1.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Интерактивный зал в историческом парке на ВДНХ",
        #                               url="https://center-game.com/histpark")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_3_1.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Интерактивный Атлас профессий Сбера и НИУ ВШЭ",
        #                               url="https://center-game.com/sber_atlas")], 1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        #     img = open('./img/about_1_3.jpg', 'rb')
        #     inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
        #         [InlineKeyboardButton(text="Кейс М.Видео-Эльдорадо под ключ",
        #                               url="https://center-game.com/mvideoacademy")],
        #         1))
        #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=img, reply_markup=inlineReplyMarkup)
        #
        # elif (buttonValue == 'right'):
        #     if (query.from_user.username in scoreBase):
        #         scoreBase[query.from_user.username] += 10
        #         query.edit_message_text(text="Правильно!✅", reply_markup=None)
        #     else:
        #         query.edit_message_text(text="Вам нужно сначала зарегистрироваться, нажав /start", reply_markup=None)
        #
        #
        # elif (buttonValue == 'wrong'):
        #     if (query.from_user.username in scoreBase):
        #         query.edit_message_text(text="Неправильно!❌", reply_markup=None)
        #     else:
        #         query.edit_message_text(text="Вам нужно сначала зарегистрироваться, нажав /start", reply_markup=None)


def menuBuilder(buttons, n_cols, headerButtons=None, footerButtons=None):
    menu = [buttons[i: i + n_cols] for i in range(0, len(buttons), n_cols)]

    if (headerButtons):
        menu.insert(0, [headerButtons])

    if (footerButtons):
        menu.append([footerButtons])

    return menu


def echo(update, context):
    if update.message:
        if update.message.text:
            update.message.reply_text(f'Я пока не знаю, что на это ответить :(')


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
               InlineKeyboardButton(
                   text="Предварительно обработанные данные, годные для принятия управленческих решений",
                   callback_data='right'),
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

    buttons = [InlineKeyboardButton(text="Минимальные средние издержки меньше, чем предельные издержки",
                                    callback_data='wrong'),
               InlineKeyboardButton(text="Цена меньше, чем минимальные средние переменные издержки",
                                    callback_data='right'),
               InlineKeyboardButton(text="Цена меньше, чем средние постоянные издержки", callback_data='wrong'),
               InlineKeyboardButton(text="Цена меньше, чем минимальные переменные издержки", callback_data='wrong')]

    replyMarkup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Вопрос 2\nВ коротком периоде фирма с целью максимизировать прибыль или "
                                  "минимизировать убытки не должна производить товар, если:",
                             reply_markup=replyMarkup)

    buttons = [
        InlineKeyboardButton(text="Равновесие рынка труда нарушается из-за влияния профсоюзов", callback_data='wrong'),
        InlineKeyboardButton(text="Безработица характеризуется «естественным» уровнем", callback_data='wrong'),
        InlineKeyboardButton(text="Безработица препятствует нормальному функционированию рынка труда",
                             callback_data='wrong'),
        InlineKeyboardButton(text="Безработица невозможна, если на рынке труда существует равновесие",
                             callback_data='right')]

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
        if (i == 1):
            text += "🥇"
        elif (i == 2):
            text += "🥈"
        elif (i == 3):
            text += "🥉"

        text += "\n"
        i += 1
        if (i > 10):
            break

    context.bot.send_message(chat_id=update.effective_chat.id, text=str(text))


if __name__ == '__main__':
    App(TOKEN).run()
    #
    # scoreBase = {}
    #
    # updater = Updater(token=TOKEN, use_context=True)
    #
    # dispatcher = updater.dispatcher
    #
    # startHandler = CommandHandler('start', firstStart)
    #
    # aboutHandler = MessageHandler(Filters.text("О нас"), about)
    # contactHandler = MessageHandler(Filters.text("Контакты"), contact)
    # serviceHandler = MessageHandler(Filters.text("Услуги"), services)
    # backHandler = MessageHandler(Filters.text("Назад"), start)
    #
    # kursesHandler = MessageHandler(Filters.text("Курсы"), kurses)
    # backkHandler = MessageHandler(Filters.text("Назaд"), services)
    #
    # modul1Handler = MessageHandler(Filters.text("Информационные системы в организации"), course1_moduls)
    # course_1_1_Handler = MessageHandler(Filters.text("Информация и информационные технологии"), course_1_modul_1)
    # course_1_2_Handler = MessageHandler(Filters.text("Правовые информационные системы"), course_1_modul_2)
    # course_1_3_Handler = MessageHandler(Filters.text("Информационные технологии и структура управления"),
    #                                     course_1_modul_3)
    #
    # modul2Handler = MessageHandler(Filters.text("Микроэкономика"), course2_moduls)
    # course_2_1_Handler = MessageHandler(Filters.text("Введение в микроэкономику"), course_2_modul_1)
    # course_2_2_Handler = MessageHandler(Filters.text("Предприятие (Фирма)"), course_2_modul_2)
    # course_2_3_Handler = MessageHandler(Filters.text("Издержки и доходы предприятия"), course_2_modul_3)
    #
    # modul3Handler = MessageHandler(Filters.text("Волновая физика"), course3_moduls)
    # course_3_1_Handler = MessageHandler(Filters.text("Упругие волны скорость энергия"), course_3_modul_1)
    # course_3_2_Handler = MessageHandler(Filters.text("Стоячая волна эффект Доплера"), course_3_modul_2)
    # course_3_3_Handler = MessageHandler(Filters.text("Электромагнитные волны световая волна"), course_3_modul_3)
    #
    # backkkHandler = MessageHandler(Filters.text("Нaзaд"), kurses)
    #
    # kurses1Handler = MessageHandler(Filters.text("Домашнее задание"), hm_course)
    # modul11Handler = MessageHandler(Filters.text("Тест по теме \"Информационные системы в организации\""),
    #                                 hm_course1_test)
    # modul22Handler = MessageHandler(Filters.text("Тест по теме \"Микроэкономика\""), hm_course2_test)
    # modul33Handler = MessageHandler(Filters.text("Тест по теме \"Волновая физика\""), hm_course3_test)
    # buttonHandler = CallbackQueryHandler(button)
    #
    # statisticHandler = MessageHandler(Filters.text("Статистика"), statistic)
    #
    # echoHandler = MessageHandler(Filters.text & (~Filters.command), echo)
    #
    # dispatcher.add_handler(startHandler)
    # dispatcher.add_handler(aboutHandler)
    # dispatcher.add_handler(contactHandler)
    # dispatcher.add_handler(serviceHandler)
    # dispatcher.add_handler(backHandler)
    # dispatcher.add_handler(buttonHandler)
    #
    # dispatcher.add_handler(kursesHandler)
    # dispatcher.add_handler(backkHandler)
    #
    # dispatcher.add_handler(modul1Handler)
    # dispatcher.add_handler(course_1_1_Handler)
    # dispatcher.add_handler(course_1_2_Handler)
    # dispatcher.add_handler(course_1_3_Handler)
    #
    # dispatcher.add_handler(course_2_1_Handler)
    # dispatcher.add_handler(course_2_2_Handler)
    # dispatcher.add_handler(course_2_3_Handler)
    #
    # dispatcher.add_handler(course_3_1_Handler)
    # dispatcher.add_handler(course_3_2_Handler)
    # dispatcher.add_handler(course_3_3_Handler)
    #
    # dispatcher.add_handler(modul2Handler)
    # dispatcher.add_handler(modul3Handler)
    # dispatcher.add_handler(backkkHandler)
    #
    # dispatcher.add_handler(kurses1Handler)
    # dispatcher.add_handler(modul11Handler)
    # dispatcher.add_handler(modul22Handler)
    # dispatcher.add_handler(modul33Handler)
    #
    # dispatcher.add_handler(statisticHandler)
    #
    # dispatcher.add_handler(echoHandler)
    #
    # updater.start_polling()
