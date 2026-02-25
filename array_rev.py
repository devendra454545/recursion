# Reversing array without using recursion(using for loop)
# 
# def rev(arr):
#     n = len(arr)//2
#     for i in range(n+1):                    
#         temp = arr[i]                     #<-----(Swapping without tuple unpacking)    
#         arr[i] = arr[len(arr)-i-1]        #----->(Tuple unpacking arr[i],arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i] )
#         arr[len(arr)-i-1] = temp
#     return arr
# arr=[1,2,3,4,5,6]
# print(rev(arr))
# 
# Using reverse function
# arr.reverse()
# print(arr)
# 
# Using slicing (array[start : stop : step])
# rev = arr[::-1]
# print(rev)
# 
# Now, finally we'll reverse the array using Recursion(Using Two Pointers)

def arrRev(arr,left,right):
    
    if left >= right:
        return
    
    arr[left],arr[right] = arr[right],arr[left]
    arrRev(arr,left+1,right-1)
    return arr

arr=[1,2,3,4,6]
print(arrRev(arr,0,len(arr)-1))



