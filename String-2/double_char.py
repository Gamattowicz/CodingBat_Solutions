''' Python 3.9
6.11.2020


Given a string, return a string where for every char in the original,
there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree' '''


def double_char(str):
    string = ''
    for i in str:
        string += i*2
    return string
