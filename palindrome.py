def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)


def is_palindrome(n):
    if n < 0:
        return False   # Negative numbers are not palindrome
    return n == reverse_number(n)


# Test
num = 121
print(is_palindrome(num))