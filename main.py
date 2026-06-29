while True:
    
    print("\n=== Calculator ===\n")
    
    try:

        a=float(input("Enter the first number: ")) 
        b=float(input("Enter the second number: "))   
    
        print("what kind of operation do you want to perform:\npress + for addition\npress - for subtraction\npress * for multiplication\npress / for division")
    
        o= input("Enter operation: ")
        match o:
            case"+":
                print(f"the result is : {a+b}")
            case"-":
                print(f"the result is : {a-b}")
            case"*":
                print(f"the result is : {a*b}")
            case"/":
                print(f"the result is : {a/b}")
            case _:
                print("Invalid operations")
    except Exception as e:
        print("Enter a valid value of a and b")