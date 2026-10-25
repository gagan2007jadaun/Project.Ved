# Day 4 - Student Profile Builder

class student:
    def __init__(self, name, course, study_hours):
        self.name = name
        self.course = course
        self.study_hours = study_hours
    # calculate weekly study hours
    def weekly_hours(self):
        return self.study_hours * 7
    # Display student details or informations
    def display_info(self):
        print("Student Name: ", self.name)
        print("Student Course: ", self.course)
        print("Student study hours: ", self.study_hours)
        print("Student weekly study hours: ", self.weekly_hours())

# student details
student1 = student("Gagan", "CSE AI ML", 5)
student2 = student("Sunny", "CSE AI ML", 4)

# display student details
print("==== First Student ====")
student1.display_info()

print()

print("==== Second Student ====")
student2.display_info()

'''
class Student: — student objects ke liye blueprint banata hai.
__init__() — object ke attributes initialise karta hai.
self — current student object ke data ko access karta hai.
weekly_hours() — calculation karke result return karta hai.
'''