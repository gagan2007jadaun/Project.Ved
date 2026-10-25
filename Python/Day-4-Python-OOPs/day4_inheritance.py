# Inheritance
'''Inheritance OOP ka ek important concept hai. Isse hum ek existing class ke attributes aur methods ko reuse karke nayi class bana sakte hain. Isse code duplication kam hota hai.
'''
'''
Maan le, Project VED mein hum do types ke users banana chahte hain:
- Student
- AIResearcher
Dono ke paas name aur course jaise common attributes ho sakte hain. AI researcher ke paas model training jaise extra behaviour bhi ho sakte hain.

Inheritance se hum common features parent class mein rakh sakte hain aur specific features child class mein add kar sakte hain
'''

# PARENT CLASS
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("My name is", self.name)

# CHILD CLASS
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
    def show_course(self):
        print("My course is", self.course)

# ANOTHER CHILD CLASS
class AIResearcher(Person):
    def __init__(self, name, research_area):
        super().__init__(name)
        self.research_area = research_area
    def show_research(self):
        print("Research Area:", self.research_area)

student = Student("GAGAN", "CSE AI ML")
researcher = AIResearcher("SUNNY", "LANGUAGE MODELS")

print("===== STUDENT =====")
student.introduce()
student.show_course()

print("\n===== AI RESEARCHER =====")
researcher.introduce()
researcher.show_research()

'''
class Student(Person):

Iska matlab Student class, Person ki child class hai. Student parent ka introduce() method inherit kar sakta hai.

super().__init__(name)

Ye parent class ka constructor call karta hai, jisse name initialise ho jaata hai. Is tarah same code dobara likhne ki zaroorat nahi hoti.

Extra methods

Student ka show_course() aur AIResearcher ka show_research() unki apni specialised functionality hai.'''