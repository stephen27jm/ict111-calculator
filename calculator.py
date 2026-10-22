while True:
 print("simple calcutator")
 num1 = float(input("Enter first number:"))
 operator = input("Enter operator (+, -, *, /): ")
 num2 = float(input("Enter second number: "))
 if operator == "+":
    answer = num1 + num2
 elif operator == "-":
    answer = num1 - num2
 elif operator == "*":
    answer = num1 * num2
 elif operator == "/":
    answer =  num1 / num2
 else:
    answer = "invalid operator"
 print("answer:", answer)
 again = input("Do you want to calculator again? (yes/no): ")
 if again.lower() != "yes":
    print("calculator closed.") 
    break 