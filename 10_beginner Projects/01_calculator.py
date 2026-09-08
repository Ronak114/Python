try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))


    c=input("Enter operation (+, -, *, /,%): ")

    match c:
        case "+":
            print(a+b)
        case "-":
                print(a-b)
        case "*":
                print(a*b)
        case "/":
                print(a/b)
        case "%":
                print(a%b)
        case "_":
                print("Enter valid operator")

except Exception as e:
       print("Enter valid no")
