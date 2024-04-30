import telebot
from telebot import types
correct_answers = 0
total_answers = 0
bot = telebot.TeleBot('6402408609:AAFeGSbCz8nYGd5avU-fj1Z-VGy4h_Geupg')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/test')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/informations')
    markup.row(btn2)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)
@bot.message_handler(commands=['test'])
def test(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/Что такое Amadeus и история развития компании')#
    markup.row(btn1)
    btn2 = types.KeyboardButton('/Архитектура системы, подсистемы и модули, используемые программы')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/Взаимодействие, интерфейсы и примеры оформления документов компании Amadeus')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Наш тест состоит из 3 частей',reply_markup=markup)
@bot.message_handler(commands=['informations'])
def handle_informations(message):
    url = 'https://docs.google.com/document/d/1Vshyw0-J_wLBI8oW0CLUb5PmYNo67cV7rUwFKQhr2ns/edit'
    bot.send_message(message.chat.id, f'Ссылка на документ: {url}')

@bot.message_handler(commands=['Что'])
def Цель(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/1.1вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/1.2вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/1.3вопрос')
    markup.row(btn3)
    btn1 = types.KeyboardButton('/1.4вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/1.5вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/1.6вопрос')
    markup.row(btn3)
    btn1 = types.KeyboardButton('/1.7вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/1.8вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/1.9вопрос')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Эта часть про историю и цели компании Amadeus', reply_markup=markup)
@bot.message_handler(commands=['Архитектура'])
def Архитектура(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/2.1вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/2.2вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/2.3вопрос')
    markup.row(btn3)
    btn4 = types.KeyboardButton('/2.4вопрос')
    markup.row(btn4)
    btn5 = types.KeyboardButton('/2.5вопрос')
    markup.row(btn5)
    btn1 = types.KeyboardButton('/2.6вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/2.7вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/2.8вопрос')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Эта часть про Взаимодействие, интерфейсы и примеры оформления документов компании Amadeus', reply_markup=markup)
@bot.message_handler(commands=['Взаимодействие,'])
def взаимодействие(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/3.1вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/3.2вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/3.3вопрос')
    markup.row(btn3)
    btn4 = types.KeyboardButton('/3.4вопрос')
    markup.row(btn4)
    btn5 = types.KeyboardButton('/3.5вопрос')
    markup.row(btn5)
    btn1 = types.KeyboardButton('/3.6вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/3.7вопрос')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/3.8вопрос')
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Эта часть про Архитектура системы, подсистемы и модули, используемые программы', reply_markup=markup)

@bot.message_handler(commands=['1.1вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.1a')
    btn2 = types.KeyboardButton('1.1b')
    btn3 = types.KeyboardButton('1.1c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.2вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Что такое Amadeus?\n a)Amadeus — это это современный банк, который работает в онлайн-режиме.\n b)Amadeus — это международная компания, занимающаяся разработкой и поставкой программно-технических решений для индустрии туризма и гостеприимства.\n c)Amadeus — это американская корпорация, которая занимается разработкой и поддержкой веб-поисковика, а также предоставляет множество других сервисов, таких как YouTube, Gmail, Maps и другие.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.1b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.1a' or message.text == '1.1c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ответ записан')
@bot.message_handler(commands=['1.2вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.2a')
    btn2 = types.KeyboardButton('1.2b')
    btn3 = types.KeyboardButton('1.2c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.3вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Какая цель и назначение компании?\n a)Способствовать развитию и повышению эффективности туристической отрасли путем предоставления инновационных сервисов, технологий и высококачественных услуг.\n b)Привлекать средства от населения и компаний в виде депозитов, предоставлять кредиты физическим и юридическим лицам.\n c)Предоставлять платформы для общения и обмена информацией между людьми, зарабатывать деньги через рекламу и платные услуги.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.2a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.2b' or message.text == '1.2c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.3вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.3a')
    btn2 = types.KeyboardButton('1.3b')
    btn3 = types.KeyboardButton('1.3c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.4вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Какие задачи у компании?\n a)Разработка и поддержка систем бронирования авиабилетов, гостиниц и других туристических услуг.\n b)Интеграция с другими системами и сервисами для упрощения процесса бронирования.\n c)Обеспечение безопасности данных клиентов и защита от мошенничества.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.3a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text in ['1.3b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text in ['1.3c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.4вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.4a')
    btn2 = types.KeyboardButton('1.4b')
    btn3 = types.KeyboardButton('1.4c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.5вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Когда основали Amadeus?\n a)1977.\n b)2003.\n c)1987.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.4c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.4a' or message.text == '1.4b')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.5вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.5a')
    btn2 = types.KeyboardButton('1.5b')
    btn3 = types.KeyboardButton('1.5c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.6вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Где основали Amadeus?\n a)Мадрид.\n b)Нью-Йорк.\n c)Париж.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.5a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.5b' or message.text == '1.5c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.6вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.6a')
    btn2 = types.KeyboardButton('1.6b')
    btn3 = types.KeyboardButton('1.6c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.7вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Кто основал компанию?\n a)Круизная компания.\n b)4 авиакомпании.\n c)Турагентство.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.6b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.6a' or message.text == '1.6c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.7вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.7a')
    btn2 = types.KeyboardButton('1.7b')
    markup.row(btn1,btn2)
    btn4 = types.KeyboardButton('/1.8вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Amadeus имеет более 800 офисов на данный момент? \n a)Да.\n b)Нет.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.7a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.7b' or message.text == '1.7c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.8вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.8a')
    btn2 = types.KeyboardButton('1.8b')
    btn3 = types.KeyboardButton('1.8c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/1.9вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Что произошло в компании в 1992 году? \n a)Первое бронирование с помощью систем Amadeus.\n b)Amadeus вышла на рынок Индии.\n c)SouthWest Airlines завершил переход на Amadeus Altéa.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.8a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.8b' or message.text == '1.8c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['1.9вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('1.9a')
    btn2 = types.KeyboardButton('1.9b')
    btn3 = types.KeyboardButton('1.9c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/2.1вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'ГВ каком году Amadeus становится мировым лидером по количеству турагентств? \n a)1995.\n b)1985.\n c)2015.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['1.9a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '1.9b' or message.text == '1.9c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')

@bot.message_handler(commands=['2.1вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('2.1a')
    btn2 = types.KeyboardButton('2.2b')
    markup.row(btn1,btn2)
    btn4 = types.KeyboardButton('/2.2вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Компания Amadeus использует архитектуру клиент-сервер для своих систем бронирования?\na)Да \nb)Нет', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.1a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.1b' or message.text == '2.1c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.2вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('2.2a')
    btn2 = types.KeyboardButton('2.2b')
    btn3 = types.KeyboardButton('2.2c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/2.3вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Из скольких уровней состоит серверная часть системы бронирования Amadeus?\n a)2 \n b)4 \n c)3', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.2c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.2a' or message.text == '2.2b')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.3вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn4 = types.KeyboardButton('/2.4вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Сопоставьте:\n1.1-й уровень\n2.2-й уровень\n3.3-й уровень \n-a База данных\n-b Серверы для приложений \n-c Приложения\nПример ответа:\n2.3)1-a.2-b.3-c', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.3)1-a.2-c.3-b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.3)1-a.2-b.3-c' or message.text == '2.3)1-b.2-a.3-c' or message.text == '2.3)1-b.2-c.3-a' or message.text == '2.3)1-c.2-a.3-b' or message.text == '2.3)1-c.2-b.3-a')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.4вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('2.4a')
    btn2 = types.KeyboardButton('2.4b')
    btn3 = types.KeyboardButton('2.4c')
    btn4 = types.KeyboardButton('2.4d')
    btn5 = types.KeyboardButton('2.4e')
    markup.row(btn1,btn2,btn3,btn4,btn5)
    btn6 = types.KeyboardButton('/2.5вопрос')
    markup.row(btn6)
    bot.send_message(message.chat.id, f'Какие средства связи используются для коммуникации между клиентами и серверами в системе бронирования Amadeus? \n a)Интернет провайдеры \n b)Телеграфы \n c)Сотовые операторы \n d)Телевидение \n e)Телефонные линии', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.4a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text in ['2.4c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text in ['2.4e'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.4b' or message.text == '2.4d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.5вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn4 = types.KeyboardButton('/2.6вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Сопоставьте:\n1.Подсистема бронирования авиабилетов Amadeus Air\n2.Подсистема бронирования гостиниц Amadeus Hotel\n3.Подсистема бронирования автомобилей Amadeus Car\n-a Модуль бронирования авиабилетов на регулярные рейсы \n-b Модуль поиска и бронирования отелей Amadeus Hotel \n-c Модуль проката легковых автомобилей \nПример ответа:\n2.5)1-a.2-b.3-c', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.5)1-a.2-b.3-c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.5)1-a.2-c.3-b' or message.text == '2.5)1-b.2-a.3-c' or message.text == '2.5)1-b.2-c.3-a' or message.text == '2.5)1-c.2-a.3-b' or message.text == '2.5)1-c.2-b.3-a')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.6вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('2.6a')
    btn2 = types.KeyboardButton('2.6b')
    btn3 = types.KeyboardButton('2.6c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/2.7вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Какие модули у подсистемы бронирования авиабилетов Amadeus Air? \n a)Модуль бронирования авиабилетов на регулярные рейсы.  \n b)Модуль поиска и бронирования отелей \n c)Модуль подбора и бронирования круизов.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.6a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.6b' or message.text == '2.6d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.7вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('2.7a')
    btn2 = types.KeyboardButton('2.7b')
    btn3 = types.KeyboardButton('2.7c')
    btn4 = types.KeyboardButton('2.7d')
    markup.row(btn1,btn2,btn3,btn4)
    btn5 = types.KeyboardButton('/2.8вопрос')
    markup.row(btn5)
    bot.send_message(message.chat.id, f'Какие модули у подсистемы бронирования авиабилетов Amadeus Car? \n a)Модуль проката легковых автомобилей \n b)Модуль бронирования хостелов \n c)Модуль проката мотоциклов \n d) Модуль бронирования чартерных рейсов.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.7a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text in ['2.7c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.7b' or message.text == '2.7d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['2.8вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('2.8a')
    btn2 = types.KeyboardButton('2.8b')
    markup.row(btn1,btn2)
    btn4 = types.KeyboardButton('/3.1вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Использует ли технологию GPS Amadeus?\n a)Да \n b)Нет.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['2.8a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '2.4b' or message.text == '2.4d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')

@bot.message_handler(commands=['3.1вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.1a')
    btn2 = types.KeyboardButton('3.1b')
    btn3 = types.KeyboardButton('3.1c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/3.2вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'С какими внешними системами бронирования авиакомпаний взаимодействует Amadeus? \n a)Tinkoff, Sberbank. \n b)Sabre, Galileo, Worldspan. \n c)Worldpay и Cybercash..', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.1b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.1a' or message.text == '3.1d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.2вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.2a')
    btn2 = types.KeyboardButton('3.2b')
    markup.row(btn1,btn2)
    btn4 = types.KeyboardButton('/3.3вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Взаимодействует ли Amadeus с системами управления гостиничными комплексами, такими как Opera, Fidelio? \n  a)Да \n b)Нет.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.2a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.2b' or message.text == '3.2d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.3вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.3a')
    btn2 = types.KeyboardButton('3.3b')
    btn3 = types.KeyboardButton('3.3c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/3.4вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'За что отвечает интерфейс Amadeus Selling Platform Connect?\n a)Amadeus Selling Platform Connect - это интерфейс, который позволяет агентам по продаже путешествий получать доступ к системе бронирования Amadeus. \n b)Amadeus Selling Platform Connect - это интерфейс, предназначенный для управления корпоративными поездками. \n c)Amadeus Selling Platform Connect - это набор программных интерфейсов, которые позволяют разработчикам интегрировать функциональность Amadeus в свои собственные приложения.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.3a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.3b' or message.text == '3.3d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.4вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.4a')
    btn2 = types.KeyboardButton('3.4b')
    markup.row(btn1,btn2)
    btn4 = types.KeyboardButton('/3.5вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Amadeus Web Services-это интерфейс предназначенный для мобильных устройств, таких как смартфоны и планшеты, включающий поиск и бронирование билетов, отслеживание рейсов и обмен сообщениями?\n a)Да \n b)Нет.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.4b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.4a' or message.text == '3.4d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.5вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.5a')
    btn2 = types.KeyboardButton('3.5b')
    btn3 = types.KeyboardButton('3.5c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/3.6вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Что такое PNR?\n a)PNR – это документ, который отправляется клиенту для подтверждения получения заявки на бронирование или другой запрос. \n b)PNR – электронный документ, содержащий информацию о пассажирах и забронированных для них услугах. \n c)PNR – это документ, удостоверяющий личность и гражданство владельца при пересечении границ государств и пребывании за границей.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.5b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.5a' or message.text == '3.5d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.6вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.6a')
    btn2 = types.KeyboardButton('3.6b')
    btn3 = types.KeyboardButton('3.6c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/3.7вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Какие данные указаны в счет-фактуре? \n a)В ней указывается сумма к оплате, номер счета, реквизиты компании и информация о выполненной работе. \n b)В ней прописываются основные характеристики продукта или услуги, цена, сроки поставки и другие условия. \n c)В ней могут быть указаны инструкции для сотрудников, рекомендации по оптимизации работы или доклад о выполненных задачах.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.6a'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.6b' or message.text == '3.6c')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.7вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.7a')
    btn2 = types.KeyboardButton('3.7b')
    btn3 = types.KeyboardButton('3.7c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/3.8вопрос')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Для чего используется служебная записка? \n a)Для заказа бронирования отеля, авиабилетов, железнодорожных билетов и других услуг. \n b)Для передачи информации по оптимизации работы и принятия решений сотрудникам о выполненных задачах. \n c)Для фиксации результатов работы и передачи клиенту или руководству компании.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.7b'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.7a' or message.text == '3.7d')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(commands=['3.8вопрос'])
def vopros(message):
    global correct_answers
    global total_answers
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('3.8a')
    btn2 = types.KeyboardButton('3.8b')
    btn3 = types.KeyboardButton('3.8c')
    markup.row(btn1,btn2,btn3)
    btn4 = types.KeyboardButton('/Итог')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Что фиксируется в отчете о выполненной работе? \n a)В нём фиксируются результатов работы и передачи клиенту или руководству компании. \n b)В отчете могут быть указаны даты выполнения работ, сведения о клиенте, основной результат работы и другие детали. \n  c)Все вышеперечисленное.', reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['3.8c'])
def check_answer(message):
    global correct_answers
    global total_answers
    total_answers += 1
    correct_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')
@bot.message_handler(func=lambda message: message.text == '3.8a' or message.text == '3.8b')
def answer_1_1_incorrect(message):
    global total_answers
    total_answers += 1
    bot.send_message(message.chat.id, 'Ваш ответ записан')

@bot.message_handler(commands=['score'])
def show_score(message):
    global correct_answers
    global total_answers
    bot.send_message(message.chat.id, f"Количество правильных ответов: {correct_answers}")
    bot.send_message(message.chat.id, f"Общее количество вопросов: {total_answers}")

@bot.message_handler(commands=['Итог'])
def results(message):
    percentage = (correct_answers / total_answers) * 100
    bot.send_message(message.chat.id, f'Вы ответили правильно на {correct_answers} из {total_answers} вопросов. Ваш результат: {round(percentage,2)}%')

bot.polling(none_stop=True)
