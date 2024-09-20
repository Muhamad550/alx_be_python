num1 = int (input("enter num1: "))
num2 = int (input("enter num2: "))
operations = input ("Choose the operation (+, -, *, /): ")

match operations: 
    case "+":
        print(f"Result: {num1+num2}")  
    case  "-":
        print(f"Result: {num1-num2}")
    case "*":
        print(f"Result: {num1*num2}")
    case "/":
        if num2 != 0:
          print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed")
    case _:
        print("Invalid operation!")

  