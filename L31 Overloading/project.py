class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")
        print("I am in grade", self.grade)

    def study(self):
        print(self.name, "is studying.")


# Create objects
student1 = Student("Alex", 14, 9)
student2 = Student("Sara", 15, 9)

# Call methods
student1.introduce()
student1.study()

print()

student2.introduce()
student2.study()