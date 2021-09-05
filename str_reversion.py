result = ''


def strReversion(s):
    global result
    if s == '':
        return ''
    else:
        return strReversion(s[1:]) + s[0]


print(strReversion('leeseokgyu'))
