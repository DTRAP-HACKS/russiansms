import os
set = [1, 10]

if os.path.isfile("config.data") != 1:
	with open('config.data', 'w') as filehandle:  
 	   for listitem in set:
 	   	filehandle.write('%s\n' % listitem)

if os.path.isfile("config.data") == 1:
	set = []
	with open('config.data', 'r') as filehandle:
	 	for line in filehandle:
	 		currentPlace = line[:-1]
	 		set.append(float(currentPlace))

def settings():
	global set
	while True:
		print("\n1 - Выходить из программы поле бомбинга: " + str(set[0]))
		print("2 - Вероятность бомбинга звонками: " + str(set[1])+"%")
		print("\n0 - Выход из этого меню и сохранение")
		menu = input()
		if menu == "0":
			with open('config.data', 'w') as filehandle:  
 			   for listitem in set:
 	  		 	filehandle.write('%s\n' % listitem)
			break
		elif menu == "1":
			if set[0] == 1: set[0] = 0
			elif set[0] == 0: set[0] = 1
		elif menu == "2":
			set[1] = float(input("\nВведите шанс звонка: "))