try :
    a = int(input("Enter the first integer value of your choice: "))
    b = int(input("Enter second integer value of your choice: "))
    print("Press + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")

    op=input("Enter any airthmetic operator that has been given above as your choice: ")
    match op:
        case "+":
            print(f"The outcome of your given values with respect to its operation is: {a + b}")
        case "-":
            print(f"The outcome of your given values with respect to its operation is: {a - b}")
        case "*":
            print(f"The outcome of your given values with respect to its operation is: {a * b}")
        case "/":
            print(f"The outcome of your given values with respect to its operation is: {a / b}")
        
except Exception as e:
    print("Enter a proper integer")