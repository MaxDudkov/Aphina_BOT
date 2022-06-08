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

                case 'next_button':
                    handler = MessageHandler(Filters.text(cmd['cmd']), self.make_next_button(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added next command")

                case 'test':
                    handler = MessageHandler(Filters.text(cmd['cmd']), self.make_test(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added test %s", cmd['name'])

                case 'stat':
                    handler = MessageHandler(Filters.text(cmd['cmd']), self.make_stat(cmd))
                    dispatcher.add_handler(handler)
                    logging.info("added test %s", cmd['name'])

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
            self.last_command[upd.message.from_user.username] = cmd['name']
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
            self.last_command[upd.message.from_user.username] = cmd['name']
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

    def make_next_button(self, cmd):
        def callback_funk(upd, ctx):
            next_q = {}
            exit = False
            for c in self.config['commands']:
                if (c['name'] == self.last_command[upd.message.from_user.username]) and (c['type'] == 'test'):
                    if c.get('next_q', False):
                        last_test_q = c['next_q']
                    else:
                        ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы завершили тест")
                        exit = True
                        last_test_q = c['prev_screen']
                    break
            print(last_test_q)
            for c in self.config['commands']:
                if c['name'] == last_test_q:
                    next_q = c
                    break

            self.last_command[upd.message.from_user.username] = last_test_q
            if(exit):
                replyMarkup = ReplyKeyboardMarkup(
                    menuBuilder([KeyboardButton(x) for x in next_q['buttons']], next_q['buttons_count']))

                text = next_q['text'].format(msg=upd.message)
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text=text, reply_markup=replyMarkup)

            else:
                buttons = []
                # print(str(next_q))
                for vrnt in next_q['variants']:
                    buttons.append(InlineKeyboardButton(text=vrnt['text'], callback_data=vrnt['val']))

                reply_markup = InlineKeyboardMarkup(menuBuilder(buttons, 1))
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text=next_q['question'], reply_markup=reply_markup)

        return callback_funk

    def make_test(self, cmd):
        buttons = []
        for vrnt in cmd['variants']:
            buttons.append(InlineKeyboardButton(text=vrnt['text'], callback_data=vrnt['val']))

        reply_markup = InlineKeyboardMarkup(menuBuilder(buttons, 1))

        def callback_funk(upd, ctx):
            self.last_command[upd.message.from_user.username] = cmd['name']
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=cmd['question'], reply_markup=reply_markup)

        return callback_funk

    def make_stat(self, cmd):
        def callback_funk(upd, ctx):
            text = "Вот наши лучшие пользователи👑:\n"
            top = []
            top = sorted(self.score_base, key=self.score_base.get)
            top.reverse()
            i = 1
            # print(str(top))
            for acc in top:
                text += str(i) + ". "
                text += str(acc) + "     " + str(self.score_base[acc])
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

            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=str(text))
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
                        reply_markup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Далее")], 1))
                        query.edit_message_text(text=btn['message'], reply_markup=None)
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Идем дальше ?", reply_markup=reply_markup)

                    case 'test_right':
                        if query.from_user.username in self.score_base.keys():
                            self.score_base[query.from_user.username] += 10
                        else:
                            self.score_base[query.from_user.username] = 10

                        reply_markup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Далее")], 1))
                        query.edit_message_text(text=btn['message'], reply_markup=None)
                        context.bot.send_message(chat_id=update.effective_chat.id, text="Идем дальше ?", reply_markup=reply_markup)


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



# def statistic(update, context):
#     text = "Вот наши лучшие пользователи👑:\n"
#     top = []
#     top = sorted(scoreBase, key=scoreBase.get)
#     top.reverse()
#     i = 1
#     # print(str(top))
#     for acc in top:
#         text += str(i) + ". "
#         text += str(acc) + "     " + str(scoreBase[acc])
#         if (i == 1):
#             text += "🥇"
#         elif (i == 2):
#             text += "🥈"
#         elif (i == 3):
#             text += "🥉"
#
#         text += "\n"
#         i += 1
#         if (i > 10):
#             break
#
#     context.bot.send_message(chat_id=update.effective_chat.id, text=str(text))
#

if __name__ == '__main__':
    App(TOKEN).run()