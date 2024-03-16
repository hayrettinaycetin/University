original_tuple_1 = (4, 3, 2, 2, -1, 18)
original_tuple_2 = (2, 4, 8, 8, 3, 2, 9)



def tuple_multiplication(x):
    result =1
    for i in range(len(x)):
        result = result * x[i]  
    print(result)

tuple_multiplication(original_tuple_1)
tuple_multiplication(original_tuple_2)