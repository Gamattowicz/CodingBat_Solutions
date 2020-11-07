''' Python 3.9
3.11.2020


Given a string, return a new string
where "not " has been added to the
front. However, if the string already
begins with "not", return the string
unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad' '''


def not_string(str):
    x = str.startswith("not")
    if x:
        return str
    else:
        return 'not '+str
