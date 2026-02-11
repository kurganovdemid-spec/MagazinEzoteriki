import telebot, time
from telebot.types import *
from telebot.types import InlineKeyboardButton as IB
import random
import textEzotika

token = "8343344087:AAGHaKLd6-zHu1o73rDUVStlM1XUUG3XHXc"
bot = telebot.TeleBot("8343344087:AAGHaKLd6-zHu1o73rDUVStlM1XUUG3XHXc")

@bot.message_handler(['start'])
def start(msg: Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, False)
    kb.row("Магический шар")
    kb.row("Хрустальный шар")
    kb.row("Книга «Гадаем на кофейной гуще»")
    kb.row("Руны")
    bot.send_message(msg.chat.id, "Добро пожаловать в магазин эзотерики, нажмите на один из четырёх товаров на клавиатуре.", reply_markup=kb)
    bot.register_next_step_handler(msg, magicball)
    print(msg.chat.id)

@bot.message_handler(['info'])
def info(msg: Message):
    bot.send_message(msg.chat.id, "Магазин Эзотерики - это телеграм бот, предлагающий множество товаров по теме Эзотерической сферы. ")

def magicball(msg: Message):
    if msg.text == "Магический шар":
        bot.send_message(msg.chat.id, "Задавайте свой вопрос.")
        bot.register_next_step_handler(msg, registermagicball)
    if msg.text == "Хрустальный шар":
        kb = telebot.types.ReplyKeyboardMarkup(True, True)
        kb.row("Узнать далёкое прошлое")
        kb.row("Узнать настоящее")
        kb.row("Узнать далёкое будущее")
        gif = open("../crystal-ball-dribble.gif", "rb")
        bot.send_document(msg.chat.id, gif, caption="Давай погадаем, выбери вариант ответа:", reply_markup=kb)
        bot.register_next_step_handler(msg, register_crystal_ball)


    if msg.text == "Книга «Гадаем на кофейной гуще»":
        kb = telebot.types.InlineKeyboardMarkup()
        for page in range(1, 7):
            kb.row(IB(f"Страница {page}", callback_data=f"page_{page}"))
        kb.row(IB("Вернуться", callback_data="kniga_menu"))
        gif1 = open("../old-book.gif", "rb")
        bot.send_document(msg.chat.id, gif1, caption="Вот самая старая книга которая у нас есть.", reply_markup=kb)
    if msg.text == "Руны":
        photo = open("../руныНорабочие.jpg", "rb")
        bot.send_photo(msg.chat.id, photo, caption="Вот руны, которые мы сейчас имеем, напишите название руна который вы хотите преобрести.")
        bot.register_next_step_handler(msg, register_runi)

@bot.callback_query_handler()
def callback_handler(call: CallbackQuery):
    if call.data.startswith("page"):
        kb = telebot.types.InlineKeyboardMarkup()
        kb.row(IB("Назад", callback_data="kniga_return"))
        kb.row(IB("Вернуться", callback_data="kniga_menu"))
        data = call.data.split("_")
        text = textEzotika.data[f"text{data[1]}"]
        bot.edit_message_caption(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    if call.data == "kniga_return":
        kb = telebot.types.InlineKeyboardMarkup()
        for page in range(1, 7):
            kb.row(IB(f"Страница {page}", callback_data=f"page_{page}"))
        bot.edit_message_caption("Вот самая старая книга которая у нас есть.", call.message.chat.id, call.message.message_id, reply_markup=kb)
    if call.data == "kniga_menu":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)


def registermagicball(msg: Message):
    kb = telebot.types.ReplyKeyboardMarkup(True, True)
    kb.row("Узнать ответ")
    bot.send_message(msg.chat.id, "Духи дешёвого магического шара готовы ответить на ваш вопрос, узнать ответ?", reply_markup=kb)
    bot.register_next_step_handler(msg, answermagicball)

def answermagicball(msg: Message):
    if msg.text == "Узнать ответ":
        blablabla = ["да", "нет", "может быть", "скорее нет"]
        bot.send_message(msg.chat.id, f"Духи отвечают: {random.choice(blablabla)}.")
        time.sleep(1)
        start(msg)

def register_crystal_ball(msg: Message):


    vremena_future = ["через 5 лет", "через 10 лет", "через 1 секунду"]
    events_future = ["всё будет хорошо", "всё будет плохо", "будет просто ужасающе", "будет всё круто"]
    prichina_future = [", потому-что ты устроишся дворником.", ", потому-что ты выиграешь в лотореи.", ", потому-что ты станешь президентом, но тебя казнят.", ", потому-что ты продолжишь жить своей жизнью."]

    vremena_past = ["5 лет назад", "10 лет назад", "в прошлой жизни", "1 секунду назад"]
    events_past = ["всё было хорошо", "всё было плохо", "было просто ужасающе", "было всё круто"]
    prichina_past = [", потому-что ты устроился дворником.", ", потому-что ты выиграл в лотореи.",
                       ", потому-что ты стал президентом, но тебя казнили.",
                       ", потому-что ты продолжал жить своей жизнью."]

    vremena_present = ["вот прямо сейчас", "в районе последних тысячалетий"]
    events_present = ["всё хорошо", "всё плохо", "просто ужасающе", "всё круто"]
    prichina_present = [", потому-что ты дворник.", ", потому-что ты участвуешь в лотореи.",
                       ", потому-что ты становишся президентом, но боишся, что тебя казнят.",
                       ", потому-что ты продолжаешь жить своей жизнью."]


    if msg.text == "Узнать далёкое прошлое":
        bot.send_message(msg.chat.id, f"окак, шар что-то говорит вам: '{random.choice(vremena_past)} {random.choice(events_past)} {random.choice(prichina_past)}'")

    if msg.text == "Узнать настоящее":
        bot.send_message(msg.chat.id, f"окак, шар что-то говорит вам: '{random.choice(vremena_present)} {random.choice(events_present)} {random.choice(prichina_present)}'")

    if msg.text == "Узнать будущее":
        bot.send_message(msg.chat.id, f"окак, шар что-то говорит вам: '{random.choice(vremena_future)} {random.choice(events_future)} {random.choice(prichina_future)}'")

    time.sleep(5)
    start(msg)

def register_runi(msg: Message):
    bot.send_message(5011459957, f"Пользователь {msg.from_user.username} подаёт заявку на покупку руна, свяжитесь с ними.")
    bot.send_message(msg.chat.id, "Ваша заявка передана в работу.")
    start(msg)

bot.infinity_polling()