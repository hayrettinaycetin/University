my_list1 = ['a','b','b','a']
my_list2 = ['a','c','b','d']
my_list3 = ['abi','asd','asd']
my_list4 = ['assa']


def polindrom(x):
    reversed_list = x[::-1]
    if x == reversed_list:
        print("True")
    else:
        print("False")


polindrom(my_list1)
polindrom(my_list2)
polindrom(my_list3)
polindrom(my_list4)
