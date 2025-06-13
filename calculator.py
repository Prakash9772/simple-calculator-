print("1 - add (+)")
print("2 - subtract (-)")
print("3 - multiply (*)")
print("4 - divide (+)")
print("5 - modulo (%)")
option = int(input("chosec an opration:"))

if(option in [1, 2, 3, 4, 5]):
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number:"))
if (option == 1) :
    print("Result:",num1 + num2)
elif (option == 2) :
    print("Result:",num1 - num2)
elif (option == 3):
    print("Result:",num1 * num2)
elif (option == 4):
    print("Result:",num1 / num2)
elif (option == 5):
    print("Result", num1%num2)
else:
    print("Invalid input, please choose 1 to 5.")