import telebot
from django.contrib.auth.models import User
from ...models import UserTG, Flags

bot = telebot.TeleBot(
    "6187649922:AAE6QwdrWIgva_SFWT_qsCsqrsNCsj_A0VU",
    parse_mode=None
)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "введи свой логин в формате: login: <логин> или логин: <логин> без скобок")

@bot.message_handler(content_types=['text'])
def bind_TG(mesage):
    header, content = mesage.text.split(': ')
    if header.upper() == 'login'.upper() or header == 'логин'.upper():
        res = User.objects.get(username=content)
        if res:
            user = res
        UserTG.objects.create(user=user, TG_id=mesage.chat.id)
        bot.reply_to(mesage, 'ваш телеграм успешно привязан')
    else:
        bot.reply_to(mesage, 'неизвестный синтаксис')

bot.infinity_polling()
