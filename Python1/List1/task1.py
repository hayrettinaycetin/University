import random
random_number = random.randrange(1,10)

while True:
    number = input("Please enter a number between 1 to 9 ")
    if not number.isdigit():
        print("Please enter a numeric value ")
    else:
        number = int(number)
        if number == random_number:
            break
        else:
            continue
            
print("Well Guess")





