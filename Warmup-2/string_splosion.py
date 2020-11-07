''' Python 3.9
4.11.2020


Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab' '''


def string_splosion(str):
    string = ''
    for i in range(len(str)):
        string += str[0:i+1]
    return string


print(string_splosion('Code'))
