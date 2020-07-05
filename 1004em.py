a = 0
b = 0
o = 0
while True:    
    prg = (input()).split(' ')
    print(prg)
    if prg[0] == 'lda':
        a = int(prg[1])
        print(a, b, o)
    if prg[0] == 'ldb':
        b = int(prg[1])
        print(a, b, o)
    if prg[0] == 'add':
        o = a+b
        print(a, b, o)
    if prg[0] == 'sub':
        o = a-b
        print(a, b, o)
    if prg[0] == 'and':
        o = a&b
        print(a, b, o)
    if prg[0] == 'or':
        o = a|b
        print(a, b, o)
    if prg[0] == 'xor':
        o = a**b
        print(a, b, o)
    if prg[0] == 'nand':
        o = ~(a&b)
        print(a, b, o)
    if prg[0] == 'nor':
        o = ~(a|b)
        print(o)
    if prg[0] == 'xnor':
        o = ~(a**b)
        print(a, b, o)