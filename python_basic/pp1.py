num1 = int(input("enter your age"))
num2 = int(input("enter your age"))
operation = input("enter the operation you want to perform")
match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)