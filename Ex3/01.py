def doixung(x):
    a = []
    for i in x:
        if i == i[::-1]:
            a.append(i)
        return a
    b = 'aaadaaa'
    print(doixung(b))
