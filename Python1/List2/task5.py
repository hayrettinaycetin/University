def reading_from_file(filename):
    f = open(filename, "r")
    print(f.read())

def writing_to_file():
    f = open("test_file2","w")
    f.write("my_list2 = [1,3,5,7,9]")
    f.close()


reading_from_file("test_file.txt")
writing_to_file()