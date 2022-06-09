import secrets
import time
import sched


class AbstractGame(object):

    def process(self, upd, ctx, user_ctx, key):
        pass


class DiceGame(AbstractGame):

    def process(self, upd, ctx, user_ctx, key):

        try:
            bet = int(key)
        except Exception:
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы ввели не число :(\nПопробуйте еще раз!")
            return

        if bet > user_ctx.score:
            ctx.bot.send_message(chat_id=upd.effective_chat.id,
                                     text="У вас нет столько очков, ведите сумму поменьше!")
        else:
            ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Ваши кубики:", reply_markup=None)
            user_score = ctx.bot.send_dice(upd.message.from_user.id).dice.value
            user_score += ctx.bot.send_dice(upd.message.from_user.id).dice.value
            # ctx.bot.send_message(chat_id=upd.effective_chat.id,
            # text="Сумма ваших кубиков:" + str(user_score), reply_markup=None)

            ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Мои кубики:", reply_markup=None)
            bot_score = ctx.bot.send_dice(upd.message.from_user.id).dice.value
            bot_score += ctx.bot.send_dice(upd.message.from_user.id).dice.value
            # ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Сумма моих кубиков:" + str(bot_score),
            #                      reply_markup=None)

            if bot_score > user_score:
                # def send_result():
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Я победила! :)",
                                     reply_markup=None, timeout=4)
                coef = -1
            elif bot_score == user_score:
                # def send_result():
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="У нас ничья!",
                                     reply_markup=None, timeout=4)
                coef = 0
            else:
                # def send_result():
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы победили!",
                                     reply_markup=None, timeout=4)
                coef = 1

            # s = sched.scheduler(time.time, time.sleep)
            # s.enter(time.monotonic() + 4000000000000, 1, send_result())
            # s.run()
            user_ctx.add_score(coef * bet)


class GallowsGame(AbstractGame):

    word_base = ['слово', 'виселица']

    def get_random_word(self):
        return secrets.choice(self.word_base)

    def is_guessed(self, word):
        for l in word:
            if not l[1]:
                return False

        return True

    def in_string(self, word):
        str = ""
        for l in word:
            if l[1]:
                str += l[0]
            else:
                str += "_"

        return str

    def is_letter_in_word(self, word, letter):
        upd = False
        for l in word:
            if l[0] == letter:
                if l[1] == 1:
                    return -1
                l[1] = 1
                upd = True

        if upd:
            return 1

        return 0

    def get_lives(self, lives):
        str = ""
        for i in range(lives):
            str += "❤"
        for i in range(9-lives):
            str += "💔"

        return str


    def process(self, upd, ctx, user_ctx, key):

        if not ('gallow_word' in user_ctx.get_state().keys()) or (not user_ctx.get_state()['gallow_word']):
            try:
                bet = int(key)
            except Exception:
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы ввели не число :(\nПопробуйте еще раз!")
                return

            if bet > user_ctx.score:
                ctx.bot.send_message(chat_id=upd.effective_chat.id,
                                     text="У вас нет столько очков, ведите сумму поменьше!")
                return

            else:
                new_word = []
                for letter in self.get_random_word():
                    new_word.append([letter, 0])
                user_ctx.set_state('gallow_word', new_word)
                user_ctx.set_state('gallow_lives', 9)
                # print(str(new_word))
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Я загадала слово - " + self.in_string(new_word))
                ctx.bot.send_message(chat_id=upd.effective_chat.id,
                                     text="Введите букву", reply_markup=None)

        else:
            word = user_ctx.get_state()['gallow_word']
            if self.is_letter_in_word(word, key) == 1:
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Правильно")

            elif self.is_letter_in_word(word, key) == -1:
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы уже называли эту букву!")

            elif self.is_letter_in_word(word, key) == 0:
                lives = user_ctx.get_state()['gallow_lives']
                user_ctx.set_state('gallow_lives', lives-1)
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Неправильная буква!")
                if not lives:
                    ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы проиграли :(")
                    user_ctx.set_state('game', 'default')

            if self.is_guessed(word):
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Вы выйграли!")
                user_ctx.set_state('game', 'default')

            else:
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Текущее слово - " + self.in_string(word))
                ctx.bot.send_message(chat_id=upd.effective_chat.id, text=self.get_lives(user_ctx.get_state()['gallow_lives']))


class CasinoGame(AbstractGame):

    def process(self, upd, ctx, user_ctx, key):
        pass