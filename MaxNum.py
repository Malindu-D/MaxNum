number1 = int(input("Enter 1st Number: "))
number2 = int(input("Enter 2nd Number: "))
number3 = int(input("Enter 3rd Number: "))

if number1>number2:
    if number1>number3:
        print("Max number is:",number1)
    else:
        print("Max number is:",number3)
else:
    if number2>number3:
        print("Max number is:",number2)
    else:
        print("Max number is:",number3)
