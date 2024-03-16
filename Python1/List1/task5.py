input = input("Please enter your binary numbers ")
binary_numbers= input.rsplit(",")

decimal_numbers = []

for binary_number in binary_numbers:
    decimal_number = int(binary_number,2)
    decimal_numbers.append(decimal_number)

divisible_by_five = []

for decimal_number in decimal_numbers:
    if decimal_number % 5 == 0:
        divisible_by_five.append(decimal_number)
    else:
        pass
print(f"Your Binary Numbers:{binary_numbers}")
print(f"Decimal Numbers:{decimal_numbers}")
print(f"Divisible by Five{divisible_by_five}")
    







    
