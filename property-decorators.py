class Person:
    def __init__(self, age):
        self._age = age # we have to define getter and setters for age i.e. _age

    @property
    def age(self):  # getter for age
        return self._age * 2

    @age.setter
    def age(self, age):  # setter for age
        if 1 <= age <= 6:
            self._age = age
        else:
            raise ValueError("Age must be b/w 1 and 6")

person = Person(2)
print(person.age)
person.age = 8