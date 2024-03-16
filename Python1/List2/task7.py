x = float(input("Please enter your dividend "))
y = float(input("Please enter your divisor "))

def divide_numbers(dividend, divisor):
    if int(divisor) == 0:
        print("Cannot divide by zero")
    else:
        print(round(float(dividend)/float(divisor),2))

divide_numbers(x,y)