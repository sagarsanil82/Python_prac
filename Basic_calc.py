# #print("Enter the first number")
# num1=int(input("Enter the first number"))

# #print("Enter the second number")
# num2=int(input("Enter the second number"))

# #print("Select the operation you want to perform: 1) Add 2) Sub 3)Mul 4)Div")
# OPR=input("Select the operation you want to perform: 1) Add 2) Sub 3)Mul 4)Div")

# match OPR:
#     case "1":
#         print(num1+num2)
#     case "2":
#         print(num1-num2)
#     case "3":
#         print(num1*num2)
#     case "4":
#         print(num1%num2)
#     case _:
#         print("Select a OPeration")

###################### String###########


String=input("Enter your string")

# print(f"Length of the string is : {len(String)}")
# print(f"Reverse of the String is : {String[::-1]}")

# count=0
# for charr in String:
#     if charr.lower() in "aeiou":
#         count=count+1
    

# print(f"Count is:{count}")

# if (String==String[::-1]):
#     print("It is  a palindrome")
# else:
#     print("It is not a palindrome")

numm=0
chap=0
emp=0

for hog in String:
    if hog.isnumeric():
        numm+=1
    if hog in " ":
        emp+=1
    if hog.isalpha():
        chap+=1


print(f"NUmber={numm},Empty={emp},Char={chap}")
##################Palindrome ##############

