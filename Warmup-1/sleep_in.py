''' Python 3.9 
03.11.2020

The parameter weekday is True if it is a weekday, and the parameter vacation
is True if we are on vacation. We sleep in if it is not a weekday or
we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True'''


def sleep_in(weekday, vacation):
    if not weekday and vacation:
        return True
    elif not weekday and not vacation:
        return True
    elif weekday and not vacation:
        return False
    else:
        return True
