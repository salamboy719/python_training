import arithemetic

def calculator():
    while True:
        try:
            first_num = float(input("Enter First number: "))
            second_num = float(input("Enter second number: "))

            print("Simple Calculator")
            print("-" * 20)
            print("Enter 1 for addition")
            print("Enter 2 for Subtraction")
            print("Enter 3 for Multiplication")
            print("Enter 4 for Division")

            choice =  int(input("Enter your choice: "))

            if choice == 1:
                print(arithemetic.addition(first_num, second_num))
                break
            elif choice == 2:
                print(arithemetic.subtraction(first_num, second_num))
                break
            elif choice == 3:
                print(arithemetic.multiplication(first_num, second_num))
                break
            elif choice == 4:
                print(arithemetic.division(first_num, second_num))
            else:
                print("Invalid Choice")
                break
        except ValueError:
            print("Invalid Input. Enter a numeric Value!")

calculator()