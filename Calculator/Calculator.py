num1 = float(input("Please enter first number : "))
num2 = float(input("Please enter secound number : "))
my_operation = input("Please enter your operation : ")

print("-----> RESULT <-----")

match my_operation:
    case "+":
        print(f"Sum {num1} and {num2} : {(num1 + num2)}")
    case "-":
        print(f"Dif {num1} and {num2} : {(num1 - num2)}")
    case "*":
        print(f"Multi {num1} and {num2} : {(num1 * num2)}")
    case "/":
        print(f"Div {num1} and {num2} : {(num1 / num2)}")
    case _:
        print(f"Sorry, Your operation ({my_operation}) not supported ! ")

print("-----> END - THANKS FOR USE MY CALCULATOR <-----")
