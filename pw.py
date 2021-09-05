text = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ']

ary = []
for i in text:
    ary.append(
        chr((int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2))))

print(''.join(ary))
