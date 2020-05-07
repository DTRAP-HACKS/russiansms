def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

def generate(mode, name):
	f = open(name)
	file = "import requests\n\ndef send(serv, _phone):\n"
	q = count_lines(name) - 1
	for i in range(count_lines(name)):
		line = f.readline()
		if line[:2] == "p:":
			file += "    " + line[3:]
		elif line[:2] == "c:": print(line[3:])
		else: file += "    if serv == " + str(q) + ": requests." + line
		q -= 1
	if mode == "s":
		sms = open("sms.py", "w")
		sms.write(file)
		sms.close
	if mode == " c":
		calls = open("calls.py", "w")
		calls.write(file)
		calls.close
	
generate("s", "database.arsdat")