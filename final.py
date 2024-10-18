
# ---------------String Reversal (increment loop)----------------------

# def NewR(strN):
#     newSTRR=""
#     for i in range(0,len(strN)):
#         newSTRR=strN[i]+newSTRR
#     return newSTRR
# strN=input("enter a nuw str")
# resul=NewR(strN)
# print(resul)



# reversed sentance---------------

# def Reversal_loop(nstr, i, s1):
#     if i == len(s1):
#         return nstr
#     nstr = s1[i] + nstr
#     return Reversal_loop(nstr, i + 1, s1)
# s1 = input("enter a new string : ")
# result = Reversal_loop("", 0, s1)
# print(result)


# ---------------String Reversal (recursion) --------------


# def Reverse(n):
#     str=''
#     for i in n:
#         str=i+str
#     return str
# n=str(input('enter a string'))    
# Reversed=Reverse(n)
# print(Reversed)
# if n==Reversed:
#     print('polyndrome')
# else:
#     print('not a polyndrm')



# vowel = ['a', 'e', 'i', 'o', 'u']
# word = str(input('enter a str'))
# count = 0
# for character in word:
#     if character in vowel:
#         count += 1
# print(count)


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = str(input('enter a str'))
# count = 0
# for character in word:
#     if character not in vowel:
#         count += 1
# print(count)


# max number finding-------------

# numberList = [15, 85, 35, 89, 125]

# maxNum = numberList[0]
# for num in numberList:
#     if maxNum < num:
#         maxNum = num
# print(maxNum)


number=[eval(x) for x in input('enter a number').split()]
maxNum=number[0]
for i in number:
    if maxNum < i:
        maxNum=i
print(maxNum)        


# min number finding------------

# numberList = [15, 85, 35, 89, 125, 2]

# minNum = numberList[0]
# for num in numberList:
#     if minNum > num:
#         minNum = num
# print(minNum)


# numberes=[eval(x) for x in input('enter a values').split()]
# minNum=numberes[0]
# for i in numberes:
#     if minNum>i:
#         minNum=i
# print(minNum)        


# # fing mid ele in list------------

# numList = [1, 2, 3, 4, 5]
# midElement = int((len(numList)/2)) 
# print(numList[midElement])



# # Anagrams or not-------------------

# str1 = str(input('enter a str'))
# str2 = str(input('enter a str'))

# str1 = list(str1.upper())
# str2 = list(str2.upper())
# str1.sort(), str2.sort()

# if(str1 == str2):
#     print("Anagram")
# else:
#     print("not a anagram")


# str1=str(input('enter a string'))
# str2=str(input('enter a string'))

# str1=list(str1.upper())
# str2=list(str2.upper())
# str1.sort(),str2.sort()

# if str1==str2:
#     print('anagram')
# else:
#     print('not a anagram')    