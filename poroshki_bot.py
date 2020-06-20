# -*- coding: utf-8 -*-

import telebot
import random
import json

bot = telebot.TeleBot('850202086:AAE1wLCKmrIPXdTyohRNtOZu8eUnEbWnGvg')


def opener(filename):
    with open(filename) as file:
        text = json.load(file)
    return text

@bot.message_handler(commands = ['info'])
def info(message):
    bot.send_message(message.chat.id, text = 'Порошок - маленькое смешное четверостишие, в котором рифмуется 2 и 4 строки, вот только в четвёртой строке всего два слога. Впервые они появились в 2011 году в интернете. Автор первых порошков - Алексей Соловьёв. Многие порошки бывают злободневными, многие нет - но они все очень смешные. \nВ первой и третьей строке порошка - 9 слогов, во второй - 8, в четвёртой - всего 2. \nЭтот бот будет присылать вам порошок на одну из предложенных тем - какую вы выберете. Порошки генерируются программой из текстов произведений, однако из-за того, что программа тяжеловата, вам приходят уже готовые (только самые лучшие!) порошки. К сожалению, наш бот ещё маленький, а техника не безупречна, поэтому ударения не везде точные. Надеюсь, что вам понравится наш бот!')

@bot.message_handler(commands = ['start'])
def hello(message):
    mark_up = telebot.types.ReplyKeyboardMarkup()
    mark_up.row('Руслан', 'Новости', 'Земфира')
    mark_up.row('Лорка', 'Смешарики', 'Рандом')
    mark_up.row('Кроссовер')
    bot.send_message(message.chat.id, text = 'Пс, не хочешь немного порошков? Выбери один из фандомов: \n"Руслан и Людмила" А.С.Пушкина \nПоследние новости \nТексты песен Земфиры \nСтихотворения Федерико Гарсия Лорки\nПесенки и стихотворения из Смешариков\nили же доверься великой силе Рандома! \n А что такое "Кроссовер"? Узнаешь, если нажмёшь! \nЕсли хочешь узнать про бота больше - пиши в сообщения /info!', reply_markup = mark_up)


@bot.message_handler()
def get_filename(message):
    #print(message)
    try:
        text = opener(message.text + '.json')
        poem = random.choice(text)
        bot.send_message(message.chat.id, text = poem)
    except Exception:
        bot.send_message(message.chat.id, text = 'Попробуй ещё раз!')

bot.polling(none_stop = True)
