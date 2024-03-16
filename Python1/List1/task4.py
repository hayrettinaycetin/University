def even_or_odd(input):
    input = int(input)
    if input % 2 == 0:
       print("Its even")
    else:
        print("Its odd") 



def being_prime(number):

    import math
    number = int(number)
def is_prime(number):
    import math
    number = int(number)
    if number == 1 or number == 2:
          print("Not prime")    
   
    elif number % 2 == 0 or number % 3 == 0:
        print("Not prime")
    else:
   
        for i in range(5, int(math.isqrt(number)) + 1, 6):
            if number % i == 0 or number % (i + 2) == 0:
                print("Not prime")

        print("Its prime")
            
def discriminant(input):
    print("SOLUTION OF EQUATION")
    print("2x^2 *(-5*A*x)+100")
    a = 2
    b = -5*int(input)
    c = 100
    delta = int((b**2) - (4*a*c))
    if delta > 0:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        print("Two real solutions:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        print("One real solution:")
        print("x1 =", x1)
    else :
        x1 = -b / (2 * a)
        print("One real solution:")
        print("x1 =", x1)
result =input("A = ")

try:
    number = float(result)
    even_or_odd(number)
    is_prime(number)
    discriminant(number)
except :
    print("This is not a valid number.")
