import os

fav_phones = []

if os.path.isfile("phones.data") != 1:
	with open('phones.data', 'w') as filehandle:  
 	   for listitem in fav_phones:
 	   	filehandle.write('%s\n' % listitem)

if os.path.isfile("phones.data") == 1:
	with open('phones.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		fav_phones.append(currentPlace)

def return_phones():
	for i in range(int(len(fav_phones)/2)):
		print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
	_phone = fav_phones[int(input("\n"))*2]
	return _phone
	
def save_phones():
	while True:
		for i in range(int(len(fav_phones)/2)):
			print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
		print("\n1 - Добавить номер\n2 - Удалить номер\n0 - Выйти")
		_menu = input()
		if _menu == "0": break
		if _menu == "1":
			fav_phones.append(input("Введите номер: "))
			fav_phones.append(input("Введите метку для номера: "))
		if _menu == "2":
	 		delete_phones = int(input("Введите номер номера, который вы хотите удалить: "))
	 		fav_phones.pop(delete_phones*2)
	 		fav_phones.pop(delete_phones*2)
		with open('phones.data', 'w') as filehandle:
			for listitem in fav_phones:
				filehandle.write('%s\n' % listitem)