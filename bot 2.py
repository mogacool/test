import telebot

token = "5930949534:AAG_EUFQL5WMtHhqXtMuP3E8Tv2FNuwxVj4"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def greeting(message):
    welcome_text = f"Привет, {message.from_user.first_name}, этот телеграм бот поможет тебе выбрать твою певую электрогитару. " \
                   "Готов узнать что-то новое? " \
                   "Да - /help"
    bot.send_message(message.chat.id, welcome_text)

# 5930949534:AAG_EUFQL5WMtHhqXtMuP3E8Tv2FNuwxVj4

@bot.message_handler(commands=['tezarius'])
def greeting(message):
    welcome_text1 = "/brig - бридж;  "
    bot.send_message(message.chat.id, welcome_text1)

    welcome_text2 = "/grif - гриф;  "
    bot.send_message(message.chat.id, welcome_text2)

    welcome_text3 = "/kolki - колки;  "
    bot.send_message(message.chat.id, welcome_text3)

    welcome_text4 = "/porochek - порожек;  "
    bot.send_message(message.chat.id, welcome_text4)

    welcome_text5 = "/gnezdo - гнездо 'Джек';  "
    bot.send_message(message.chat.id, welcome_text5)

    welcome_text6 = "/zvuk - звукосниматели;  "
    bot.send_message(message.chat.id, welcome_text6)

    welcome_text7 = "/nakladka - накладка или пикгард;  "
    bot.send_message(message.chat.id, welcome_text7)

    welcome_text8 = "/korpus - корпус электрогитары;  "
    bot.send_message(message.chat.id, welcome_text8)

    welcome_text9 = "/perek - переключатель звукоснимателей;  "
    bot.send_message(message.chat.id, welcome_text9)

    welcome_text10 = "/krutilki - ручки громкости и тона;  "
    bot.send_message(message.chat.id, welcome_text10)

    welcome_text11 = '/golova - голова грифа'
    bot.send_message(message.chat.id, welcome_text11)

@bot.message_handler(commands=['help'])
def help(message):
    welcome_text = "Что ты хочешь узнать первым ?" \
                   "Что вообще из себя предстовляет электрогитара - /gitara ." \
                   "Виды корпусов для электрогитары - /korpus . " \
                   "Какие аксесуары стоит взять для электрогитары - /acses . " \
                   "Комбоуселители(то без чего твоя гитара не будет работать) - /kombik" \
                   "Фирмы выпускающие электрогитар - /firma"
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['gitara'])
def greeting(message):
    welcome_text = "Электрогита́ра — электрический музыкальный инструмент, разновидность гитары, имеющая электромагнитные звукосниматели, преобразующие колебания металлических струн в звук. " \
                   "Электрогитары делятся по многим признакам: по форме корпуса, количеству струн, комлпектации звукоснимателей. " \
                   "Для общего предсталения, рассмотрим пример одной из самых популярных электрогитар в мире: Fender Stratocaster. " \
                   "Про какой элемент тебе хотелось бы узнать больше? "
    bot.send_message(message.chat.id, welcome_text)

    welcome_text1 = "/brig - бридж;  "
    bot.send_message(message.chat.id, welcome_text1)

    welcome_text2 = "/grif - гриф;  "
    bot.send_message(message.chat.id, welcome_text2)

    welcome_text3 = "/kolki - колки;  "
    bot.send_message(message.chat.id, welcome_text3)

    welcome_text4 = "/porochek - порожек;  "
    bot.send_message(message.chat.id, welcome_text4)

    welcome_text5 = "/gnezdo - гнездо 'Джек';  "
    bot.send_message(message.chat.id, welcome_text5)

    welcome_text6 = "/zvuk - звукосниматели;  "
    bot.send_message(message.chat.id, welcome_text6)

    welcome_text7 = "/nakladka - накладка или пикгард;  "
    bot.send_message(message.chat.id, welcome_text7)

    welcome_text8 = "/korpus - корпус электрогитары;  "
    bot.send_message(message.chat.id, welcome_text8)

    welcome_text9 = "/perek - переключатель звукоснимателей;  "
    bot.send_message(message.chat.id, welcome_text9)

    welcome_text10 = "/krutilki - ручки громкости и тона;  "
    bot.send_message(message.chat.id, welcome_text10)

    mem_file = open("gitara.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file)

#  5930949534:AAG_EUFQL5WMtHhqXtMuP3E8Tv2FNuwxVj4
# БРИДЖ --------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['brig'])
def greeting(message):
    welcome_text = "Бридж это такое устройство в гитаре, через которое проходят струны до того как попадут в корпус. " \
                   "Основными функциями бриджа являются: " \
                   "Регулировка высоты струн; " \
                   "Изменение длины струны (мензура); " \
                   "Подтяжка / ослабление струн; " \
                   "Раскачка при помощи ручки тремоло (если оно есть). " \
                    'Какие бывают бриджы? ' \
                    'В музыкальном мире выделяют два основных типа бриджей: ' \
                    'Фиксированный тип;  ' \
                    'Тремоло системы. ' \
                    'Рассказать про /tremolo - тремоло или /fiks - фиксированный ?'
    bot.send_message(message.chat.id, welcome_text)

@bot.message_handler(commands=['tremolo'])
def greeting(message):
    welcome_text = "Для данных струнодержателей характерно широкое разнообразие видов, что позволяет подобрать инструмент под любые запросы и уровень мастерства. " \
                   "Одни из самых популярных видов тремоло систем: "
    bot.send_message(message.chat.id, welcome_text)
    welcome_text1 = "Bigsby. Это родоначальник всех тремоло. Применяют данный бридж чаще всего на электрогитарах фирмы Gretsch. " \
                    "Данный струнодержатель также популярен и на электрогитарах фирм Gibson и Fender. "
    bot.send_message(message.chat.id, welcome_text1)
    mem_file = open("trem1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file)

    welcome_text2 = "Vintage tremolo. Данный бридж впервые устанавливался на электрогитарах - Fender Stratocaster. " \
                    "Это были струнодержатели на шести болтах, позволяющие понижать либо повышать строй гитары. " \
                    "Но вот подтяжка нот при этом была незначительной, т.к. при активном пользовании рычага, электрогитара быстро теряла строй."
    bot.send_message(message.chat.id, welcome_text2)

    mem_file1 = open("trem2.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

    welcome_text3 = 'Wilkinson. ' \
                    'Это следующее поколение от Vintage. Данный бридж позволяет свободно работать рычагом благодаря зажиму струн именно на самой «машинке». '
    bot.send_message(message.chat.id, welcome_text3)

    mem_file2 = open("wilk.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)

    welcome_text4 = 'Floyd Rose. ' \
                    'Тремоло от Флойда Роуза (компания Kramer), которое предпочитают многие профессиональные музыканты. ' \
                    'Позволяет как понижать, так и повышать строй, а также получать различные музыкальные эффекты. ' \
                    'Отпугивающей стороной системы является тяжелая настройка.'
    bot.send_message(message.chat.id, welcome_text4)

    mem_file2 = open("floyd.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)

    welcome_text5 = 'Вернемся к составу гитары? - /gitara . ' \
                    'Или рассказать про фиксированный бридж? - /fiks'
    bot.send_message(message.chat.id, welcome_text5)


@bot.message_handler(commands=['fiks'])
def greeting(message):
    welcome_text = "Среди фиксированных бриджей выделяют два: " \
                   "Tune-o-matic и " \
                   "Hardtail. " \
                   "Tune-o-matic - тип бриджа, разработанный в середине прошлого столетия. Имеет два подвида: "
    bot.send_message(message.chat.id, welcome_text)
    welcome_text1 = "1. С креплением сквозь корпус. Наиболее простой вид, но придающий гитарному звуку особую красоту и уникальность. "
    bot.send_message(message.chat.id, welcome_text1)
    mem_file = open("fiks.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file)


    welcome_text2 = "2. С креплением со стоп-баром. Такой вид струнодержателя можно увидеть на электрогитарах Gibson. "
    bot.send_message(message.chat.id, welcome_text2)
    mem_file1 = open("stop.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

    welcome_text3 = 'А что про Hardtail? ' \
                    'Крепление струн при таком держателе происходит сквозь весь корпус, благодаря чему на выходе получается отличный резонанс и уникальная отдача дерева.' \
                    ' Данный бридж является предшественником системы Vintage Tremolo, отличаясь от неё только отсутствием рычага. '
    bot.send_message(message.chat.id, welcome_text3)

    mem_file2 = open("hard.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)

    welcome_text4 = "Теперь узнаем про тремоло? " \
                    "/tremolo ." \
                    " Или вернемся к составу гитары? - /gitara "
    bot.send_message(message.chat.id, welcome_text4)
# --------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['grif'])
def greeting(message):
    welcome_text = "Гриф представляет собой часть гитары в виде длинной деревянной рукоятки специальной формы и размера, к которой прижимаются струны для того, чтобы изменить длину их колеблющейся части и соответственно высоту извлекаемого звука. " \
                   "После порожка - /porochek, идёт часть грифа, которую многие называют головой - /golova. " \
                   "На голове грифа расположены колки - /kolki, механизм который закрепляет другой конец струны, а так же регулирует её натяжение. "
    bot.send_message(message.chat.id, welcome_text)

    welcome_text2 = "По сути грифы отличаются друг от друга только материалом, из которого они изготовлены,  головой и количеством ладов(обычно 22 либо 24). "
    bot.send_message(message.chat.id, welcome_text2)


@bot.message_handler(commands=['golova'])
def greeting(message):
    welcome_text1 = "Четкого разделения на виды грифов нет, но я бы, всё-таки, раздлелил их на два вида: "
    bot.send_message(message.chat.id, welcome_text1)

    welcome_text2 = "Гриф с колками на одной стороне "
    bot.send_message(message.chat.id, welcome_text2)
    mem_file1 = open("fenderG.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)
    mem_file2 = open("iban1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)

    welcome_text3 = "Гриф с колками по обе стороны "
    bot.send_message(message.chat.id, welcome_text3)
    mem_file3 = open("gibson.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file3)
    mem_file4 = open("sgr.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file4)

    welcome_text4 = "Кстати, вы наверное заметили, что все производители гитар пишут название своей фирмы именно на голове грифа "
    bot.send_message(message.chat.id, welcome_text4)
    welcome_text5 = 'Вернемся к грифу - /grif, или продожлим изучать другие элементы электрогитары - /gitara ?'
    bot.send_message(message.chat.id, welcome_text5)

# -----------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['kolki'])
def greeting(message):
    welcome_text = "Колки это механизм, с помощью которого струны крепится к грифу, с помощью колков также регулируется натяжение струн. Существует довольно много видов колков, но я расскажу про основные, их которых исходят другие виды: "
    bot.send_message(message.chat.id, welcome_text)

    welcome_text2 = "Открытые колки - /open"
    bot.send_message(message.chat.id, welcome_text2)

    welcome_text3 = "Закрытые колки - /broke"
    bot.send_message(message.chat.id, welcome_text3)

    welcome_text4 = "Локовые колки - /lok"
    bot.send_message(message.chat.id, welcome_text4)


@bot.message_handler(commands=['open'])
def greeting(message):
    welcome_text = "Открытые колки отличаются тем что их механизм полностью открыт, такие колки очень удобны для обслуживания, но они не защищены от физических воздействий."
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("kolk1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

@bot.message_handler(commands=['broke'])
def greeting(message):
    welcome_text = "По механизму не отличается от открых колков, однако в отиличии от них механзим закрыт крышкой. Такие колки уже больше защищены от физических воздействий, но обслуживать их сложнее чем открытые."
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("kolk4.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

@bot.message_handler(commands=['lok'])
def greeting(message):
    welcome_text = "Локовые колки похожи на закрытые, но они отличаются дополнительным механизмом, который надежно фиксирует струну в механизме, вероятность проскальзывания струны с такого колка равна нулю. А еще в такие колки можно намного быстрее устанавливать струны. К минусам таких колков можно отнести цену, которая обычно в 2-3 раза больше других моделей."
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("kolk3.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

#---------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['porochek'])
def greeting(message):
    welcome_text = "Порожек представляет их себя маленькую пластинку которая служит для создания высоты между грифом и струнами. Из за слишком низкого порожка струны буду излишне ударятся об лады и звенеть, а при слишком высоком порожке струны будут слишком высоко и зажимать струны будет сложно и не удобно."
    bot.send_message(message.chat.id, welcome_text)
    welcome_text2 = "Порожки можно разделить по материалам из которого они делаются: "
    bot.send_message(message.chat.id, welcome_text2)

    welcome_text3 = "Порожки из кости - /bone"
    bot.send_message(message.chat.id, welcome_text3)

    welcome_text4 = "Порожки из графита - /grafit"
    bot.send_message(message.chat.id, welcome_text4)

    welcome_text5 = "Латунные порожки - /latun"
    bot.send_message(message.chat.id, welcome_text5)

    welcome_text6 = "Порожки с локовым механизмом (эти порожки отличаются не материалом с механизмом) - /lokporochek"
    bot.send_message(message.chat.id, welcome_text6)

@bot.message_handler(commands=['bone'])
def greeting(message):
    welcome_text = "Используется на большинстве винтажных электрогитар, такой порожек дает мягкое звучание без всяких призвуков. Из-за особенностей материала такие порожки сложно палировать. "
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("por1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)
    mem_file2 = open("por2.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)

@bot.message_handler(commands=['grafit'])
def greeting(message):
    welcome_text = "Графитовые порожки обсепечивают лучшее скольжение струн по порожку, а еще дают мягкое звучание струнам."
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("pork3.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

@bot.message_handler(commands=['latun'])
def greeting(message):
    welcome_text = "Латунные порожки являются самыми твердыми и долговечными, а так же дают яркое и кристальное звучание."
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("4-brass.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

@bot.message_handler(commands=['lokporochek'])
def greeting(message):
    welcome_text = "Такой порожек надежно фиксирует струны. Обычно такие порожки стоят на электрогитарах с тремоло бриджем, потому что после использования тремоло, струны не всегда встают на изначальное положение и из-за этого меняется строй гитары, а порожки с локовым механизмом предотвращают такое."
    bot.send_message(message.chat.id, welcome_text)
    mem_file1 = open("pork5.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)

#----------------------------------------------------------------------------------------------------------------------------------

#-ЭЛЕКТРОННИКА-------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(commands=['gnezdo'])
def greeting(message):
    welcome_text1 = 'Гнездо для провода - это разъём для подключения электрогитары к звуковому устройству, на всех современных гитарах стоит разъём "Джек". Обычно гнездо находится либо на верхней части корпуса, либо в боковой части.'
    bot.send_message(message.chat.id, welcome_text1)

    mem_file1 = open("gnezdo1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)
    mem_file2 = open("gnezdo2.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)
    mem_file3 = open("gnezdo3.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file3)
    mem_file4 = open("gnezdo4.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file4)

@bot.message_handler(commands=['zvuk'])
def greeting(message):
    welcome_text1 = 'Звукосниматели - это устройство передающее звук колебания струн в устройство устройство для вывода звука. Наличие звукоснмателей одно из главных различий электрогитары и акустической гитары.'
    bot.send_message(message.chat.id, welcome_text1)

    welcome_text2 = 'Существует очень много видов звукоснимателей, но по сути их всех можно разделить на два вида - синглы и хамбакеры. Они отличаются конструкцией и звуком передаваевым в звуковое устройство'
    bot.send_message(message.chat.id, welcome_text2)

    welcome_text3 = 'рассказать про хамбакеры - /humbucker'
    bot.send_message(message.chat.id, welcome_text3)

    welcome_text4 = 'рассказать про синглы - /singl'
    bot.send_message(message.chat.id, welcome_text4)

    welcome_text5 = 'Кроме синглов и хамбакеров, звукосниматели также делятся на активные звукосниматели и неактивные.' \
                    'Рассказать про активные и пассивные - /passoractive'
    bot.send_message(message.chat.id, welcome_text5)

@bot.message_handler(commands=['humbucker'])
def greeting(message):
    welcome_text1 = 'Хамбакер - это сингл, но с двумя катушками, и соответственно двумя рядами магнитов. С такими звукоснимателями звук будет более теплым и четким, из-за большего числа магнитов звук передается более четче чем на синглах. Такие звукосниматели подходят для подхлдят для всех разновидностей рока, металла, а также для блюза и джаза.'
    bot.send_message(message.chat.id, welcome_text1)

    mem_file1 = open("humb1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)
    mem_file2 = open("humb2.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)


@bot.message_handler(commands=['singl'])
def greeting(message):
    welcome_text1 = 'Сингл - самые первый звукосниматель в истории электрогитар, у него только одна медная катушка. Такие звукосниматели имеют звонкий и яркий звук, часто такой звук называют "стеклянным". Обычно гитары с такими звукоснимателями подходят для классического рока, поп музыки, фанк и панк рока. '
    bot.send_message(message.chat.id, welcome_text1)

    mem_file1 = open("single1.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file1)
    mem_file2 = open("single2.jpg", 'rb')
    bot.send_photo(message.chat.id, mem_file2)


@bot.message_handler(commands=['passoractive'])
def greeting(message):
    welcome_text1 = 'Внешне пассивные и активные звукосниматели практически не отличаются, но они отличаются звуком и механизмом. Во первых самое первое отличие активных звукоснимателей от пассивных это наличие батарейки. То есть без батарейки активные звукосниматели работать не будут, в отличии от пассивных. ' \
                    'А чем отличается звук? У активных звукоснимателей стоят специальные магниты, которые в отличии от пассивных будут намного меньше притягивать струны, а соответсвенно и время колебания струны.'
    bot.send_message(message.chat.id, welcome_text1)

    welcome_text2 = 'Время колебания струн называют сустейном - то есть насколько долго струна будет издавать звук после удара по ней. Кроме улучшенного сустейна, активные звукосниматели передают звук точнее из-за более низкого сопротивления.'
    bot.send_message(message.chat.id, welcome_text2)

#-----------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=['korpus'])
def greeting(message):
    welcome_text = "Корпус"
    bot.send_message(message.chat.id, welcome_text)

bot.polling()



