import sms, calls
import sys
from random import randint
from time import sleep

def try_sms(_phone):
    try:
        sms.send(_phone)
        return 1
    except:
        return 0

def try_calls(_phone):
    try:
        calls.send(_phone)
        return 1
    except:
        return 0

def main(_param, _phone, _quantity, _time, _percent):
    while _quantity != 0:
        if randint(0, 100) >= _percent:
            if try_sms(_phone) == 1: _quantity -=1
        else:
            if try_calls(_phone) == 1: _quantity -=1
        sleep(_time)
        if _param == "-g": print("Осталось: " + str(_quantity))

params = []        
if __name__ == "__main__":
	 for param in sys.argv:
	 	params.append(param)
	 main(params[1], params[2], int(params[3]), float(params[4]), int(params[5]))
	
