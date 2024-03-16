class Person:
    def __init__(self,name,country,date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def age(self):
        from datetime import date
        today = date.today()
        return today.year - self.date_of_birth     

p1 = Person("John","USA",1990)
P2 = Person("Alex","UK",1995)
p3 = Person("Wiktoria","Poland",2000)
p4 = Person("Hayro","Türkiye",2003) 

john_age = p1.age()
alex_age = P2.age()
wiktoria_age = p3.age()
hayro_age = p4.age()

print(john_age)
print(alex_age)
print(wiktoria_age)
print(hayro_age)