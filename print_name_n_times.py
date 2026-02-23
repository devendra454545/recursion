def nameNTimes(n):
    if n<=0:
        return
    nameNTimes(n-1)
    print('Devendra')
nameNTimes(7)