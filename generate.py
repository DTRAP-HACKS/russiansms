import sys

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))

def generate(mode, name):
	a = 1
	f = open(name)
	file1 = ""
	file = "import requests, random\n\ndef send(_phone):\n"
	q = count_lines(name) - 1
	for i in range(count_lines(name)):
		line = f.readline()
		if line[:2] == "p:":
			file += "    " + line[3:]
		elif line[:2] == "c:": print(line[3:])
		elif line[:2] == "\n": pass
		else:
			file1 += "    if serv == " + str(q) + ": requests." + line
			if a == 1:
				b = q
				a = 0
		q -= 1
	file += "    serv = random.randint(0, " + str(b) + ")\n"
	file += file1
	if mode == "-s":
		sms = open("sms.py", "w")
		sms.write(file)
		sms.close()
	if mode == "-c":
		calls = open("calls.py", "w")
		calls.write(file)
		calls.close()

params = []
if __name__ == "__main__":
	for param in sys.argv:
		params.append(param)
	generate(params[1], params[2])
