# def Polyndrm(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=rev*10+rem
#         n//=10
#     return rev
# n=int(input('enter number'))    
# res=Polyndrm(n)
# if n==res:
#     print('polyndrom')
# else:
#     print('not a polyndrom')    


# def Polyndrm(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=rev*10+rem
#         n//=10
#     return rev
# sr=int(input('entera number'))    
# er=int(input('entera number')) 
# for i in range(sr,er+1):
#     res=Polyndrm(i)
#     if res==i:
#         print(i)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def count_palindromes_in_range(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_palindrome(num):
            count += 1
    return count

# Example usage
start = 10
end = 200
result = count_palindromes_in_range(start, end)
print(f"Number of palindrome numbers between {start} and {end}: {result}")
