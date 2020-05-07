import sms, calls
from random import randint
from time import sleep

def try_sms(_phone):
    try:
        sms.send(_phone)
        return true
    except:
        return false

def try_calls(_phone):
    try:
        calls.send(_phone)
        return true
    except:
        return false

def main(_phone, _quantity, _time, _percent):
    while _quantity != 0:
        if randint(0, 100) >= _percent:
            if try_sms(_phone) == true: _quantity -=1
        else:
            if try_calls(_phone) == true: _quantity -=1
        
        sleep(_time)