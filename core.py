import sms, calls
from random import randint
from time import sleep

def main(_phone, _quantity, _time, _percent):
	while _quantity != 0:
		if randint(0, 100) >= _percent:
			try:
				sms.send(_phone)
				_quantity -=1
		else:
			try:
				calls.send(_phone)
				_quantity -= 1
		
		sleep(_time)