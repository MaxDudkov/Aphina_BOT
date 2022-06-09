import secrets
import time
import sched


class AbstractGame(object):

    def process(self, upd, ctx, user_ctx, bet, key):
        pass


class DiceGame(AbstractGame):

    def process(self, upd, ctx, user_ctx, bet, key=None):

        ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Ваши кубики:", reply_markup=None)
        user_score = ctx.bot.send_dice(upd.message.from_user.id).dice.value
        user_score += ctx.bot.send_dice(upd.message.from_user.id).dice.value
        # ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Сумма ваших кубиков:" + str(user_score), reply_markup=None)

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
        return True


class GallowsGame(AbstractGame):

    word_base = ['слово', 'виселица']

    def get_random_word(self):
        return secrets.choice(self.word_base)

    def process(self, upd, ctx, user_ctx, bet, key):
        if not user_ctx.get_gallow_word():
            new_word = {}
            for letter in self.get_random_word():
                new_word[letter] = 0
            user_ctx.set_gallow_word(new_word)
            # print(str(new_word))


