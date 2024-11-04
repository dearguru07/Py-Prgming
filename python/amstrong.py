# def countD(n):
#     count=0
#     while n!=0:
#         n//=10
#         count+=1
#     return count
# def Amstrong(n):
#     tem=n
#     sum=0
#     power=countD(n)
#     while n!=0:
#         rem=n%10
#         sum=sum+rem**power
#         n//=10
#     if tem==sum:
#         return True
#     else:
#         return False
# n=int(input('enter a number'))        
# flag=Amstrong(n)
# if flag==True:
#     print('it is amstrong number')
# else:
#     print('not a amstgng')    



def CountD(n):
    count=0
    while n!=0:
        n//=10
        count+=1
    return count
def Amstrong(n):
    tem=n
    sum=0
    power=CountD(n)
    while n!=0:
        rem=n%10
        sum=sum+rem**power
        n//=10
    if tem==sum:
            return True
    else:
            return False
sr=int(input('enter a nunber'))    
er=int(input('enter a nunber'))
flaot=True
for i in range(sr,er+1):
    if flaot==Amstrong(i):
        print(i)




        