num1 = int(input("Enter First Num :"))
op = input("Enter Operation to perform :")
num2 = int(input("Enter Second Num  :"))

if op == "+":
    add = num1+num2
    print("addition is :", add)

elif op == "-":
    sub = num1-num2
    print("subtraction is :", sub)

elif op == "*":
    mul = num1 * num2
    print("Multiplication is :", mul)

elif op == "/":
    div = num1 / num2
    print("Division is :", div)

else:
    print("Entered wrong operation")
