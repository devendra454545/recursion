def upToN(n):
    if n==0:
        return
    upToN(n-1)
    print(n)
upToN(10)