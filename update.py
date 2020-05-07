import requests

def update(version):
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
			print("\nОбновление завершено, откройте бомбер заново командой\npython boom.py")
			return "exit"
		elif upd_vers == version: print("Установлена последняя версия, вы прекрасны")
		elif upd_vers < version: print("Не хочешь попасть в команду?")
		else: print("Ошибка, файл обновлений не найден")
	except BaseException:
		print("Нет интернета, попробуйте позже")