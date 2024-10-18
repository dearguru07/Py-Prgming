
# str='#hello#world#to#all'
# str1=""
# str2=""
# for i in str:
#     if i=='#':
#         str1=str1+i
#     else:
#         str2=str2+i
# print(str1+str2)            


# def Reverse(n):
#     res=''
#     for i in n:
#         res=i+res
#     return res
# str=input('entere a str')    
# sol=Reverse(str)
# print(sol)



# def Reverse(n):
#     str1=''
#     str2=''
#     for i in n:
#         if i=='#':
#             str1=str1+i
#         else:
#             str2=str2+i
#     print(str1+str2)        
# str=input('entera nunmber')
# Reverse(str)

def Reverse(n):
    res=''
    for i in n:
        res=i+res
    return res
str=input('enter a str')
sol=Reverse(str)
print(sol)