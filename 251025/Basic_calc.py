#print("Enter the first number")
num1=int(input("Enter the first number"))

#print("Enter the second number")
num2=int(input("Enter the second number"))

#print("Select the operation you want to perform: 1) Add 2) Sub 3)Mul 4)Div")
OPR=input("Select the operation you want to perform: 1) Add 2) Sub 3)Mul 4)Div")

match OPR:
    case "1":
        print(num1+num2)
    case "2":
        print(num1-num2)
    case "3":
        print(num1*num2)
    case "4":
        print(num1%num2)
    case _:
        print("Select a OPeration")
