def Prime(n):
    tem=True
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            tem=False
            break
    if tem==True and n>2:
        print('prime number')
    else:
        print('not a prime')    
n=int(input('enter a number'))        
Prime(n)



# def Prime(n):
#     err=n//2
#     for i in range(2,err+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('enter a nunber'))    
# er=int(input('enter a nunber'))    
# for i in range(sr,er+1):
#     if i>1:
#         flag=Prime(i)
#         if flag==True:
#             print(i)