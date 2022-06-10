from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext import Updater
import yaml
import logging

from abstract_game import DiceGame, GallowsGame, CasinoGame

TOKEN = '5290614906:AAGYFaOjyqukQHJDwBiLfpHih-xSmS0smx4'


class Context(object):
    def __init__(self):
        self.state = {'game': 'default'}
        self.tests = []
        self.last_command = ""
        self.score = 0
        self.nickname = ""

    def set_state(self, key, state):
        self.state[key] = state

    def get_last_command(self):
        return self.last_command

    def set_last_command(self, last_command):
        self.last_command = last_command

    def get_score(self):
        return self.score

    def add_score(self, score):
        self.score += score

    def set_score(self, score):
        self.score = score

    def get_state(self):
        return self.state

    def add_test(self, test):
        self.tests.append(test)

    def get_tests(self):
        return self.tests


class App(object):
    def __init__(self, token):
        self.config = None
        self.token = token
        self.data_base = {}
        self.games = {"state_dice": DiceGame(), 'state_gallows': GallowsGame(), 'state_casino': CasinoGame()}
        logging.basicConfig(level=logging.DEBUG)

    def get_context(self, username, nickname=None):
        if username in self.data_base:
            return self.data_base[username]

        else:
            ctx = Context()
            if nickname:
                ctx.nickname = nickname
            self.data_base[username] = ctx
            return ctx

    def run(self):
        updater = Updater(token=self.token, use_context=True)
        dispatcher = updater.dispatcher

        self.config = yaml.safe_load(open('config.yml'))

        for cmd in self.config['commands']:
            if "make_" + cmd['type'] not in dir(self):
                logging.error("cant find method " + "make_" + cmd['type'])
                return

            maker = getattr(self, "make_" + cmd['type'])
            if cmd.get('command_handler', False):
                handler = CommandHandler(Filters.text(cmd['cmd']), maker(cmd))

            else:
                handler = MessageHandler(Filters.text([cmd['cmd']]), maker(cmd))

            dispatcher.add_handler(handler)
            logging.info("added handler %s", cmd['cmd'])

        buttonHandler = CallbackQueryHandler(self.button)
        echoHandler = MessageHandler(Filters.text & (~Filters.command), self.get_echo())

        dispatcher.add_handler(buttonHandler)
        dispatcher.add_handler(echoHandler)

        updater.start_polling()

    def make_default_message(self, cmd):
        if cmd.get('callback_data', False):
            if cmd.get('url', False):
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
            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_last_command(cmd['name'])
            logging.info('user %s cmd %s', upd.message.from_user.id, cmd['name'])
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=cmd['text'], reply_markup=replyMarkup)

        return callback_func

    def make_file(self, cmd):
        def callback_func(upd, ctx):
            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_last_command(cmd['name'])
            logging.info('user %s cmd %s', upd.message.from_user.id, cmd['name'])
            filename = open(cmd['file'], 'rb')
            ctx.bot.send_document(upd.effective_chat.id, filename)

        return callback_func

    def make_interactive_command(self, cmd):
        if cmd.get('callback_data', False):
            if cmd.get('url', False):
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
            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_last_command(cmd['name'])
            text = cmd['text'].format(msg=upd.message)
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=text, reply_markup=replyMarkup)

        return callback_funk

    def make_back_button(self, cmd):
        def callback_funk(upd, ctx):
            last_menu = {}
            last_screen_name = "start"
            for c in self.config['commands']:
                if c['name'] == self.get_context(upd.message.from_user.id, upd.message.from_user.username).get_last_command():
                    last_screen_name = c['prev_screen']
                    break

            for c in self.config['commands']:
                if c['name'] == last_screen_name:
                    last_menu = c
                    break

            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_last_command(last_screen_name)
            replyMarkup = ReplyKeyboardMarkup(
                menuBuilder([KeyboardButton(x) for x in last_menu['buttons']], last_menu['buttons_count']))

            text = last_menu['text'].format(msg=upd.message)
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=text, reply_markup=replyMarkup)

        return callback_funk

    def make_next_button(self, cmd):
        def callback_funk(upd, ctx):
            next_q = {}
            exit = False
            last_test_q = 'cource3_test_q1'
            for c in self.config['commands']:
                if (c['name'] == self.get_context(upd.message.from_user.id, upd.message.from_user.username).get_last_command()) and (c['type'] == 'test'):
                    if c.get('next_q', False):
                        last_test_q = c['next_q']
                    else:
                        ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы завершили тест")
                        exit = True
                        self.get_context(upd.message.from_user.id).add_test(c['test_type'])
                        last_test_q = c['prev_screen']
                    break
            # print(last_test_q)
            for c in self.config['commands']:
                if c['name'] == last_test_q:
                    next_q = c
                    break

            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_last_command(last_test_q)
            if exit:
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
        next_reply_markup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Далее")], 1))

        def callback_funk(upd, ctx):
            if cmd['test_type'] in self.get_context(upd.message.from_user.id).get_tests():
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы уже проходили этот тест!")
                return

            ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы запустили тест:\n" + cmd['cmd'], reply_markup=next_reply_markup)
            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_last_command(cmd['name'])
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=cmd['question'], reply_markup=reply_markup)

        return callback_funk

    def make_stat(self, cmd):
        def callback_funk(upd, ctx):
            text = "Вот наши лучшие пользователи👑:\n"
            top = []
            top = sorted(self.data_base.values(), key=lambda x: x.score, reverse=True)
            i = 1
            print(str(top))
            for acc in top:
                text += str(i) + ". "
                text += str(acc.nickname) + "     " + str(acc.get_score())
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

    def make_game(self, cmd):
        def callback_funk(upd, ctx):
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text=cmd['text'], reply_markup=None)
            self.get_context(upd.message.from_user.id, upd.message.from_user.username).set_state('game', cmd['state_code'])
        return callback_funk

    def button(self, update, context):
        query = update.callback_query
        buttonValue = query.data

        query.answer()

        for btn in self.config['buttons']:
            if btn['button_value'] == buttonValue:
                if btn['type'] == 'ads':
                    query.delete_message()
                    for msg in btn['messages']:
                        img = open(msg['img'], 'rb')
                        inlineReplyMarkup = InlineKeyboardMarkup(menuBuilder(
                            [InlineKeyboardButton(text=msg['text'],
                                                     url=msg['url'])], 1))
                        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img,
                                               reply_markup=inlineReplyMarkup)

                elif btn['type'] == 'test_wrong':
                    reply_markup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Далее")], 1))
                    query.edit_message_text(text=btn['message'], reply_markup=None)
                    context.bot.send_message(chat_id=update.effective_chat.id, text="Идем дальше ?", reply_markup=reply_markup)

                elif btn['type'] == 'test_right':
                    score = self.get_context(query.from_user.id).get_score()
                    self.get_context(query.from_user.id).set_score(score + 10)

                    reply_markup = ReplyKeyboardMarkup(menuBuilder([KeyboardButton("Далее")], 1))
                    query.edit_message_text(text=btn['message'], reply_markup=None)
                    context.bot.send_message(chat_id=update.effective_chat.id, text="Идем дальше ?", reply_markup=reply_markup)

    def get_echo(self):
        def callback_funk(update, context):
            user_context = self.get_context(update.message.from_user.id)
            for state in self.games.keys():
                if user_context.state['game'] == state:
                        self.games[state].process(update, context, user_context, update.message.text)
                        return

            if update.message:
                if update.message.text:
                    update.message.reply_text(f'Я пока не знаю, что на это ответить :(')

        return callback_funk


def menuBuilder(buttons, n_cols, headerButtons=None, footerButtons=None):
    menu = [buttons[i: i + n_cols] for i in range(0, len(buttons), n_cols)]

    if (headerButtons):
        menu.insert(0, [headerButtons])

    if (footerButtons):
        menu.append([footerButtons])

    return menu

if __name__ == '__main__':
    App(TOKEN).run()