# def Prime(n):
#     er=n//2
#     tem=True
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True and n>2:
#         print('Prime number')    
#     else:
#         print('not a prime')    
# n=int(input('enter a number'))
# Prime(n)


# def RangePrime(n):
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('entera number'))    
# er=int(input('entera number'))    
# for i in range(sr,er+1):
#     if i>1:
#         res=RangePrime(i)
#         if res==True:
#             print(i)


# def CountD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count=count+1
#     return count
# n=int(input('enter a number'))
# res=CountD(n)
# print(res)


# def CountD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# sr=int(input('entera number'))    
# er=int(input('entera number'))    
# for i in range(sr,er+1):
#     res=CountD(i)
#     print(i,'count of nbrs',res)



# def Reverese(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=rev*10+rem
#         n=n//10
#     return rev
# n=int(input('enter a number'))
# res=Reverese(n)
# print(res)    


# def RangeOfCount(n):
#     rev=0
#     while n!=0:
#         rem=n%10
#         rev=rev*10+rem
#         n//=10
#     return rev
# sr=int(input('entera number'))    
# er=int(input('entera number')) 
# for i in range(sr,er+1):
#     count=RangeOfCount(i)   
#     print(i,'reve is',count)