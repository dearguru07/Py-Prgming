# def CountD(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count=count+1
#     return count
# n=int(input("enter a nu ber"))    
# res=CountD(n)
# print(res)


# def CountD(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count=count+1
#     return count
# sr=int(input('entera number'))    
# er=int(input('entera number'))  
# for i in range(sr,er+1):
#     res=CountD(i)  
#     print(i,'count of digits is',res)


def CountD(n):
    count=0
    while n!=0:
        n=n//10
        count=count+1
    return count
sr=int(input('enter a number'))    
er=int(input('enter a number'))    
for i in range(sr,er+1):
    flag=CountD(i)
    print(i,'count is',flag)