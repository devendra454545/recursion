def sumOfFirstNNumbers(n):
    if n==0:
        return 0
    return n +sumOfFirstNNumbers(n-1)
    

print(sumOfFirstNNumbers(5))