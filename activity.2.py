class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am studying {self.course}.")

# Create three student objects
student1 = Student("jake", 33, "hm")
student2 = Student("celmar", 40, "criminology")
student3 = Student("sika", 29, "Information Technology")

# Call the introduce() method for each student
student1.introduce()
student2.introduce()
student3.introduce()