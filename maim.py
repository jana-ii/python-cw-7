
class person:
    name = "jana"
    age = 14
    def is_adult (self):
        if self.age  > 18:
            print('you have TOO much responsibilty')
        else:
            print('your so lucky')
first_person = person()
print(first_person.name)
print(first_person.age)
print(first_person.is_adult())


class personn:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"my name is {self.name} and i am {self.age}"

first_personn = personn("jj", 13)
print (first_personn)