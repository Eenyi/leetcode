def romanToInt(s):
    num = 0
    previous = '-'
    for e in s:
        if e=='I':
            num = num+1
        elif e=='V':
            if previous != 'I':
                num = num+5
            else:
                num = num+3
        elif e=='X':
            if previous != 'I':
                num = num+10
            else:
                num = num+8
        elif e=='L':
            if previous != 'X':
                num = num+50
            else:
                num = num + 30
        elif e=='C':
            if previous != 'X':
                num = num+100
            else:
                num = num + 80
        elif e=='D':
            if previous != 'C':
                num = num+500
            else:
                num = num + 300
        elif e=='M':
            if previous != 'C':
                num = num+1000
            else:
                num = num + 800
        previous = e
    return num
print(romanToInt("MCD"))