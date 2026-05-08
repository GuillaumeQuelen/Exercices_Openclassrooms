## Écrivez votre code ici !
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_details(self):
        print(f"Nom: {self.name}\n  Âge: {self.age}")

class Employee(Person):
    #Faire appel au paramètres précédents
    def __init__(self, name, age, salary):
        super().__init__(name, age)    #Faire appel au paramètres précédents
        self.salary = salary
    
    def display_details(self):
        super().display_details()
        print(f"  Salaire: {self.salary}")


person = Person("Julie", 28)
person.display_details()

employee = Employee("Arch", 40, 3000)
employee.display_details()