# Student Management System
class student:
    def __init__(self, name, course, study_hours):
        self.name=name
        self.course=course
        self.__study_hours=study_hours

    def get_study_hours(self):
        return self.__study_hours

    def weekly_hours(self):
        return self.__study_hours * 7

    def display_info(self):
        print("name:", self.name)
        print("course:", self.course)
        print("daily study hours:",self.__study_hours)
        print("Weekly study hours:",self.weekly_hours())

class ResearchStudent(student):
    def __init__(self,  name, course, study_hours, research_area):
        super().__init__(name, course, study_hours)
        self.research_area = research_area
    def display_info(self):
        super().display_info()
        print("Research Area:", self.research_area)

# create student objects
student1 = student("Gagagn", "CSE AIML", 4)
student2 = ResearchStudent(
    "sunny",
    "cse",
    5,
    "Language Model"
)

students = [student1, student2]

for student in students:
    print("\n====== Student Profile ======")
    student.display_info()

'''
Is project mein kya use hua?
- Classes and objects: Student profiles create kiye.
- Constructor: Har object ka initial data set kiya.
- Encapsulation: Study hours ko __study_hours attribute mein rakha aur getter method provide kiya.
- Inheritance: ResearchStudent, Student se inherit karta hai.
- Polymorphism: Dono classes ka display_info() different output deta hai.
Note: double underscore attribute Python mein name-mangling use karta hai; ye strict security mechanism nahi hai.
'''