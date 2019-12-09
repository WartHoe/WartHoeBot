import telebot
import datetime

bot = telebot.TeleBot('1051297716:AAHpeuZFPDubBYj3SObReKueoKOMwulZXBY')

tod = ('Привет!\n\nУроки на сегодня:\n')
tom = ('Привет!\n\nУроки на завтра:\n')
todk = ('Кабинеты сегодня:\n\n')
hgd = ('\nХорошего дня!')

mon = ('1)История\n2)Алгебра\n3)Алгебра\n4)Литература\n5)Русский\n6)Физика\n')
tue = ('1)Английский(Б)/Информатика\n2)Обществознание\n3)Геометрия\n4)Физ-ра\n5)Английский(З)/Информатика\n6)Физика\n')
wed = ('1)Информатика\n2)Физика\n3)Физ-ра\n4)Литература\n5)История\n6)Биология\n')
thu = ('1)Алгебра\n2)Геометрия\n3)География\n4)Английский(З)/Информатика\n5)Физика\n6)Английский(Б)/Информатика\n')
fri = ('1)Химия\n2)Литература\n3)Физика\n4)Русский язык\n5)Проектная деятельность\n6)Алгебра\n7)Физ-ра\n')
sat = ('1)Обществознание\n2)Английский(Б)/Информатика\n3)Финансовая грамотность\n4)Кубановедение\n5)ОБЖ\n6)Английский(З)/Информатика\n')
sun = ('Хэй, сегодня выходной!)')

monk = ('1)308\n2)303\n3)303\n4)202\n5)202\n6)301\n')
tuek = ('1)с/з\n2)106\n3)303\n4)101/302a\n5)112/302a\n6)301\n')
wedk = ('1)302a\n2)301\n3)с/з\n4)205\n5)106\n6)201\n')
thuk = ('1)303\n2)303\n3)310\n4)112/302a\n5)301\n6)101/302a\n')
frik = ('1)202\n2)114\n3)301\n4)114\n5)210\n6)303\n')
satk = ('1)313\n2)101/302a\n3)313\n4)313\n5)106\n6)112/302a\n')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Уроки на сегодня', 'Уроки на завтра', 'Кабинеты', 'Расписание на неделю')
    


@bot.message_handler()
def send_text(message):
    dw = datetime.datetime.today().strftime("%a")
    if (message.text == 'Уроки на сегодня') and (dw == 'Mon'):
        bot.send_message(message.chat.id, (tod + mon + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на сегодня') and (dw == 'Tue'):
        bot.send_message(message.chat.id, (tod + tue + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на сегодня') and (dw == 'Wed'):
        bot.send_message(message.chat.id, (tod + wed + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на сегодня') and (dw == 'Thu'):
        bot.send_message(message.chat.id, (tod + thu + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на сегодня') and (dw == 'Fri'):
        bot.send_message(message.chat.id, (tod + fri + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на сегодня') and (dw == 'Sat'):
        bot.send_message(message.chat.id, (tod + sat + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на сегодня') and (dw == 'Sun'):
        bot.send_message(message.chat.id, (('Сегодня выходной!') + hgd), reply_markup=keyboard1)


    if (message.text == 'Уроки на завтра') and (dw == 'Mon'):
        bot.send_message(message.chat.id, (tom + tue + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на завтра') and (dw == 'Tue'):
        bot.send_message(message.chat.id, (tom + wed + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на завтра') and (dw == 'Wed'):
        bot.send_message(message.chat.id, (tom + thu + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на завтра') and (dw == 'Thu'):
        bot.send_message(message.chat.id, (tom + fri + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на завтра') and (dw == 'Fri'):
        bot.send_message(message.chat.id, (tom + sat + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на завтра') and (dw == 'Sat'):
        bot.send_message(message.chat.id, ('Завтра выходной!' + hgd), reply_markup=keyboard1)
    elif (message.text == 'Уроки на завтра') and (dw == 'Sun'):
        bot.send_message(message.chat.id, (tom + mon + hgd), reply_markup=keyboard1)

    if (message.text == 'Кабинеты') and (dw == 'Mon'):
        bot.send_message(message.chat.id, (todk + monk + hgd), reply_markup=keyboard1)
    elif (message.text == 'Кабинеты') and (dw == 'Tue'):
        bot.send_message(message.chat.id, (todk + tuek + hgd), reply_markup=keyboard1)
    elif (message.text == 'Кабинеты') and (dw == 'Wed'):
        bot.send_message(message.chat.id, (todk + wedk + hgd), reply_markup=keyboard1)
    elif (message.text == 'Кабинеты') and (dw == 'Thu'):
        bot.send_message(message.chat.id, (todk + thuk + hgd), reply_markup=keyboard1)
    elif (message.text == 'Кабинеты') and (dw == 'Fri'):
        bot.send_message(message.chat.id, (todk + frik + hgd), reply_markup=keyboard1)
    elif (message.text == 'Кабинеты') and (dw == 'Sat'):
        bot.send_message(message.chat.id, (todk + satk + hgd), reply_markup=keyboard1)
    elif (message.text == 'Кабинеты') and (dw == 'Sun'):
        bot.send_message(message.chat.id, (('Сегодня выходной!') + hgd), reply_markup=keyboard1)
    if (message.text == 'Расписание на неделю'):
        bot.send_message(message.chat.id, ('Расписание на неделю:\n\nПонедельник:\n' + mon + '\nВторник:\n' + tue + '\nСреда:\n' + wed + '\nЧетверг:\n' + thu + '\nПятница:\n' + fri + '\nСуббота:\n' + sat), reply_markup=keyboard1)

        
    if (message.text == '/porch'):
        bot.send_message(message.chat.id, 'Порча наведена)0)')
        
    if (message.text != 'Уроки на завтра') and (message.text != 'Уроки на сегодня') and (message.text != 'Кабинеты') and (message.text != 'Расписание на неделю') and (message.text != '/porch'):
        bot.send_message(message.chat.id, 'Привет, воспользуйся клавиатурой!', reply_markup=keyboard1)

bot.polling()