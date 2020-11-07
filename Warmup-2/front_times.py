''' Python 3.9
3.11.2020


Given a string and a non-negative int n,
we'll say that the front of the string is
the first 3 chars, or whatever is there
if the string is less than length 3.
eturn n copies of the front;


front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc' '''


def front_times(str, n):
    if len(str) < 4:
        return str*n
    else:
        return str[:3]*n


print(front_times('Chocolate', 2))
