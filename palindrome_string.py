def isPalindrome(s,left,right):
    #base case  ---> main idea is that if a string passes the condition and reaches the base case then it means it is palindrome
    if left >= right:
        return True
    
    #condition  ---> if the condition fails it just gives the value as false
    if s[left] != s[right]:
        return False
    
    return isPalindrome(s, left+1, right-1)

string = 'madam'

result = isPalindrome(string,0,len(string)-1)

if result:
    print('Palindrome')
else:
    print('Not Palindrome')