from config import TOKEN
import telebot
from telebot.types import Message, ReplyKeyboardMarkup as Rkm, ReplyKeyboardRemove as Rkr, InlineKeyboardMarkup as Ikm,\
    InlineKeyboardButton as Ikb, CallbackQuery

bot = telebot.TeleBot(TOKEN)
remove_reply = Rkr()


@bot.message_handler(commands=['start'])
def start(m: Message):
    bot.send_message(m.chat.id, text='привет, как дела?')


@bot.message_handler(commands=['help'])
def my_help(m: Message):
    kb = Rkm(resize_keyboard=True, one_time_keyboard=True)
    kb.row('сколько будет 9*9?', 'как выучить стих?')
    kb.row('как посчитать среднее арифметическое?', 'как найти периметр прямоугольника?')
    bot.send_message(m.chat.id, text='чем я могу помочь?', reply_markup=kb)


@bot.message_handler(commands=['go'])
def go(m: Message):
    bot.send_message(m.chat.id, text='до Санкт Петербурга 688 км')


@bot.message_handler(commands=['sites2'])
def inline(m: Message):
    kb = Ikm()
    kb.row(Ikb('Google', url='google.com'), Ikb('Yandex', url='yandex.ru'))
    kb.row(Ikb('Market.yandex', url='market.yandex.ru'))
    kb.row(Ikb('действие 1', callback_data='Д1'))
    bot.send_message(m.chat.id, text='выбери кнопку', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback(call: CallbackQuery):
    print(call.data)
    if call.data == 'Д1':
        bot.edit_message_text('мы научились менять текст и удалять кнопки при нажатии действие 1',
                              call.message.chat.id, call.message.message_id, reply_markup=None)
    if call.data == 'Д2':
        bot.edit_message_text('мы научились удалять кнопки при нажатии действие 2',
                              call.message.chat.id, call.message.message_id, reply_markup=None)



@bot.message_handler(commands=['sites'])
def innline(m: Message):
    kb = Ikm()
    kb.row(Ikb('Fl birga', url='fl.ru'), Ikb('Rebotica', url='lk.rebotica.ru'))
    kb.row(Ikb('secret-kitchen', url='secret-kitchen.ru'), Ikb('whatsapp', url='web.whatsapp.com'))
    kb.row(Ikb('mech', url='school.mos.ru'))
    kb.row(Ikb('действие 2', callback_data='Д2'))
    bot.send_message(m.chat.id, text='какую кнопку хочешь нажать?', reply_markup=kb)


@bot.message_handler(content_types=['text'])
def text_handler(m: Message):
    msg_text = m.text.lower()
    if msg_text == 'хорошо, как у тебя?':
        bot.reply_to(m, 'отлично брат, хочешь арбуз продам 500 рублей за грамм')
    elif msg_text == 'давай брат':
        bot.reply_to(m, 'с тебя брат 1 000 000 рублей арбуз весит 2 кг')
    elif msg_text == 'пока':
        bot.reply_to(m, 'до свидания')
    elif msg_text == 'я получил 5':
        bot.send_message(m.chat.id, text='хорош')
    elif msg_text == 'сколько будет 9*9?':
        bot.send_message(m.chat.id, text='будет 81 учи таблицу умножения', reply_markup=remove_reply)
    elif msg_text == 'как выучить стих?':
        bot.send_message(m.chat.id,
                         text='Прочитать стих вслух с выражением. Использовать интонацию, паузы, мимику и жесты — '
                              'эмоциональное чтение помогает быстрее запомнить строки.'
                              'Разделить текст на небольшие смысловые отрывки — по 2–4 строчки. Работать с каждой '
                              'частью отдельно: прочитать, обсудить, повторить несколько раз. Только когда ребёнок '
                              'уверенно воспроизводит одну часть, переходить к следующей.'
                              'Использовать ассоциации. Создать ассоциативный ряд к стихотворению: рассмотреть '
                              'иллюстрации, нарисовать собственные картинки к каждому четверостишию, придумать '
                              'забавные сравнения.'
                              'Использовать движения и жесты. Придумать простые жесты или действия для каждой '
                              'строчки стихотворения.'
                              'Повторять стих через рисунки и комиксы. Каждая строфа может быть проиллюстрирована '
                              'рисунком, который отражает её содержание.',
                         reply_markup=remove_reply)
    elif msg_text == 'как посчитать среднее арифметическое?':
        bot.send_message(m.chat.id, text='нужно сложить все числа и разделить на их количество',
                         reply_markup=remove_reply)
    elif msg_text == 'как найти периметр прямоугольника?':
        bot.send_message(m.chat.id,
                         text='нужно сложить две стороны и умножить их на 2 или  сторону A умножить на 2 и сторону B '
                              'умножить на 2 и сложить их',
                         reply_markup=remove_reply)


@bot.message_handler(content_types=['audio'])
def audio_handler(m: Message):
    audio_file = m.audio
    file_id = audio_file.file_id
    file_info = bot.get_file(file_id)
    downloading = bot.download_file(file_info.file_path)
    with open(f'files/{audio_file.file_unique_id}.mp3', 'wb') as my_file:
        my_file.write(downloading)
    print('аудио скачано')


@bot.message_handler(content_types=['photo'])
def photo_handler(m: Message):
    photo_file = m.photo[-1]
    file_id = photo_file.file_id
    file_info = bot.get_file(file_id)
    downloading = bot.download_file(file_info.file_path)
    with open(f'files/{photo_file.file_unique_id}.jpg', 'wb') as my_file:
        my_file.write(downloading)
    print('фото скачано')


@bot.message_handler(content_types=['sticker'])
def sticker_handler(m: Message):
    bot.send_message(m.chat.id, text='(☞ﾟヮﾟ)☞классный стикер☜(ﾟヮﾟ☜)')


bot.infinity_polling()
