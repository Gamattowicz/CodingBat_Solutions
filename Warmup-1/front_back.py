''' Python 3.9
3.11.2020


Given a string, return a new string where
the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba' '''


def front_back(str):
    if len(str) <= 1:
        return str
    m = str[1:-1]
    return str[-1] + m + str[0]


print(front_back('rse'))
