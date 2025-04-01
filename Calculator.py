def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "5":
            print("Exiting...")
            break
        
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    print("Result:", num1 + num2)
                elif choice == "2":
                    print("Result:", num1 - num2)
                elif choice == "3":
                    print("Result:", num1 * num2)
                elif choice == "4":
                    if num2 == 0:
                        print("Cannot divide by zero!")
                    else:
                        print("Result:", num1 / num2)
            except ValueError:
                print("Please enter valid numbers!")
        else:
            print("Invalid choice! Try again.")

calculator()
