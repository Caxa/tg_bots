# -*- coding: utf-8 -*-
import telebot
from telebot import types

bot = telebot.TeleBot('6345299243:AAH4XSdulNDstSEBo6rArGfGN04USk2lykQ')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/Открыть сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/Информация')
    markup.row(btn2)
    btn3 = types.KeyboardButton('/Главное меню')
    markup.row(btn3)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)

@bot.message_handler(commands=['open_site','Открыть'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Открыть сайт госуслуги', url='https://www.gosuslugi.ru/')
    markup.row(btn1)
    bot.send_message(message.chat.id,'Сайт госуслуги',reply_markup=markup)

@bot.message_handler(commands=['informations','Информация'])
def handle_informations(message):
    bot.send_message(message.chat.id, 'Предоставление актуальной информации о процедуре регистрации прав на недвижимость в ЛНР, ДНР, Запорожской и Херсонской областях, в соответствии с законодательством Российской Федерации.')

@bot.message_handler(commands=['Главное','main_menu'])
def main_menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Регистрация прав', callback_data='registration')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Документы', callback_data='documents')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('МФЦ ', callback_data='mfc')
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton('Горячая линия Росреестра', callback_data='hotline')
    markup.row(btn4)
    btn5 = types.InlineKeyboardButton('Обратная связь', callback_data='svaz')
    markup.row(btn5)
    bot.send_message(message.chat.id, 'Выберите пункт из главного меню:', reply_markup=markup)
@bot.message_handler(commands=['QR'])
def QR(message):
    file=open('./Qr.png','rb')
    bot.send_photo(message.chat.id,file)


@bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
def main_menu_callback(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Регистрация прав', callback_data='registration')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Документы', callback_data='documents')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('МФЦ ', callback_data='mfc')
    markup.row(btn3)
    btn4 = types.InlineKeyboardButton('Горячая линия Росреестра', callback_data='hotline')
    markup.row(btn4)
    btn5 = types.InlineKeyboardButton('Обратная связь', callback_data='svaz')
    markup.row(btn5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите пункт из главного меню:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'registration')
def registration_callback(call):
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
    markup.row(btn5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Если у вас есть недвижимость (квартира, нежилое строение, дом или участок), то она должна быть зарегистрирована в Росреестре.\nК сожалению, данные о недвижимости в ЛНР, ДНР, Запорожской и Херсонской областях не полностью представлены в Росреестре, поэтому собственникам недвижимости необходимо самостоятельно обратиться в отделение МФЦ для регистрации ранее возникших прав на объекты недвижимости', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'documents')
def documents_callback(call):
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
    markup.row(btn5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Для регистрации в Росреестре прав на объекты недвижимости возьмите с собой подтверждающие права документы:\n- Акты, устанавливающие наличие, возникновение, переход, прекращение права или ограничение права и обременение объекта недвижимости;\n- Договоры (купли-продажи, мены, дарения и другие);\n- Акты (свидетельства) о приватизации;\n- Свидетельства о праве на наследство;\n- Вступившие в законную силу судебные акты;\n- Иные документы, предусмотренные Федеральным законом, ФЗ - № 218, ст.14, ч. 2.', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: call.data == 'svaz')
def registration_callback(call):
    markup = types.InlineKeyboardMarkup()
    btn5 = types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
    markup.row(btn5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Будем благодатны за пожелания по доработке данного чат-бота:\nПочта на которую можно направить электронное письмо \nevl83@mail.ru', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mfc')
def mfc_callback(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('ЛНР', callback_data='mfc_lnr')
    btn2 = types.InlineKeyboardButton('ДНР', callback_data='mfc_dnr')
    btn3 = types.InlineKeyboardButton('Херсонская область', callback_data='mfc_kherson')
    btn4 = types.InlineKeyboardButton('Запорожская область', callback_data='mfc_zaporizhia')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    btn5= types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
    markup.row(btn5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите регион, чтобы узнать адреса МФЦ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'hotline')
def mfc_callback(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('ЛНР', callback_data='ros_lnr')
    btn2 = types.InlineKeyboardButton('ДНР', callback_data='ros_dnr')
    btn3 = types.InlineKeyboardButton('Херсонская область', callback_data='ros_kherson')
    btn4 = types.InlineKeyboardButton('Запорожская область', callback_data='ros_zaporizhia')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    btn5= types.InlineKeyboardButton('Главное меню', callback_data='main_menu')
    markup.row(btn5)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите регион, чтобы узнать телефонные номера МФЦ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data =='ros_lnr')
def LNR_tel(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='hotline')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Телефоны:\n8(857) 2-50-00-90 (по общим вопросам);\n8(857) 2-50-10-45 (приёмная руководителя);\nЭлектронный адрес:\nпока не представлен', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data =='ros_dnr')
def DNR_tel(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='hotline')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Телефон: \n+7 949 500-04-51 (горячая линия);\nЭлектронный адрес: \n80_upr@rosreestr.ru', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'ros_zaporizhia')
def Zaporoz_tel(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='hotline')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Телефон: \n+7 990 133-21-71 \nЭлектронный адрес: \n85_upr@rosreestr.ru', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'ros_kherson' )
def Xerson_tel(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='hotline')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Телефон: \nпока не представлен\nЭлектронный адрес: \nпока не представлен.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mfc_lnr')
def LNR(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='mfc')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='1. г. Луганск «Центральный» (ул. В. Титова, 10)\n2. г. Луганск «Артемовский» (ул. Линева, 114)\n3. г. Луганск «Жовтневый №1» (30-й квартал, 13)\n4. г. Луганск «Жовтневый №2» (кв. 50 лет Октября, 4-А)\n5. г. Луганск, г. Счастье (ул. Ленина, 6)\n6. г. Алчевск (ул. Горького, 49)\n7. г. Антрацита и Антрацитовского района (ул. Петровского, 63)\n8. Беловодского района (пгт. Беловодск, ул. Ленина, 132)\n9. Белокуракинского района (пгт. Белокуракино, ул. Чапаева, 63А)\n10. г. Брянка (ул. Артема, 6)\n11. г. Брянка (микрорайон Тополь,3)\n12. г. Кировск (ул. Ленина, 16)\n13. г. Краснодона и Краснодонского района (г. Краснодон, ул. Микроцентр, 25) - на ремонте\n14. г. Краснодона и Краснодонского района (ул. Артема, 11)\n15. г. Красный Луч (ул. Магистральная, 62Л)\n16. г. Кременная (ул. Советская, 3)\n17. г. Лисичанск (ул. Красногвардейская, 63)\n18. Лутугинского района (г. Лутугино, ул. Дружбы, 19)\n19. Марковского района (пгт. Марковка, ул. Ленина, 22)\n20. Меловского района (пгт. Меловое, ул. Ленина, 39)\n21. Новоайдарского района (пгт. Новоайдар, ул. Ленина, 28А)\n22. Новопсковского района (пгт. Новопсков, ул. Школьная, 15Б)\n23. г. Первомайск (ул. КИМ, 14)\n24. Перевальского района (ул. Ленина, 80 Б)\n25. г. Ровеньки (ул. Коммунистическая, 6)\n26. г. Ровеньки (ул. Ленина, 19)\n27. Сватовский район (г. Сватово, пл. Советская, 25)\n28. г. Свердловск и Свердловского района ( г. Свердловск, ул. Энгельса, 43)\n29. г. Свердловск и Свердловского района (г. Свердловск, ул. Энгельса, 44)\n30. г. Северодонецк (ул. Ленина, 32А)\n31. г. Северодонецк (проспект Гвардейский, 19)\n32. Славяносербского района (пгт. Славяносербск, ул. Гагарина, 36)\n33. Станично-Луганского района (пгт. Станица Луганская, ул. Ленина, 52)\n34. Старобельского района (г. Старобельск, ул. Коммунаров, 36)\n35. г. Стаханов отделение №1 (ул. Кирова, 32)\n36. г. Стаханов отделение №2 (проспект 50 лет Октября, 8/1)\n37. Троицкий район (пгт. Троицкое, кв. Молодежный, 6)\n', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mfc_dnr')
def DNR(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='mfc')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='1. г. Донецк, пр-т Мира, д. 10А;\n2. г. Мариуполь, пр-т Мира, д. 107;\n3. г. Снежное, ул. Декабристов, д. 16;\n4. г. Макеевка, ул. Ленина, д. 80;\n5. г. Горловка, д. Герцена, д. 15\n6. г. Тельманова, ул. Мира, д. 7\n7. г. Харцызск, ул. Лазо, д. 17.\n', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mfc_zaporizhia' )
def Zaporoz(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='mfc')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='1.  Запорожская обл., г.. Мелитополь, ул.. Кирова, д. 65;\n2. Запорожская обл., г.. Бердянск, пр-кт. Труда, д. 47;\n3. Запорожская обл., г.. Мелитополь, ул.. Фрунзе, д. 19;\n4. Запорожская обл., р-н. Приморский, г.. Приморск, ул.. Центральная, д. 7;\n5. Запорожская обл., р-н. Акимовский, пгт.. Акимовка, ул.. Центральная, д. 111;\n6. Запорожская обл., р-н. Приазовский, пгт.. Приазовское, ул.. Центральная, д. 2.\n', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'mfc_kherson' )
def Xerson(call):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Назад', callback_data='mfc')
    markup.row(btn1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='1. Херсонская область, Скадовский м. о., г. Скадовск, ул. Сергеевская, д. 15;\n2. Херсонская область, Генический м. о., г. Геническ, ул. Демьяна Бедного, д. 39;\n3. Херсонская область, Новотроицкий м. о., пгт. Новотроицкое, ул. Соборная, д. 61;\n4. Херсонская область, Каланчакский м. о., пгт. Каланчак, ул. Херсонская, д. 4;\n5. Херсонская область, Чаплинский м. о., пгт. Чаплинка, ул. Парковая, д. 46;\n6. Херсонская область, Каховский м. о., г. Каховка, ул. Пушкина, д. 110;\n7. Херсонская область, Новокаховский г. о., г. Новая Каховка, ул. Первомайская, д. 25-д;\n8. Херсонская область, Херсонский м. р-н., Великокопанское с. п., с. Великие Копани, ул. Карла Маркса, д. 79;\n9. Херсонская область,  Великолепетихский м. о., пгт. Великая Лепетиха, ул. Соборная, д. 3;\n10. Херсонская область, Скадовский м. р-н, Бехтерское с. п. с.Бехтеры, ул. Благодатная, д.50.\n', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def unknown_command_handler(message):
    bot.send_message(message.chat.id, 'Извините, не поняла вашу команду. Пожалуйста, попробуйте ещё раз.')


bot.polling()

