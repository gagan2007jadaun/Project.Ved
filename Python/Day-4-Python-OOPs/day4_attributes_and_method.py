class Student:
    def __init__(self, name, course, study_hours):
        self.name = name
        self.course = course
        self.study_hours = study_hours
    def display_info(self):
        print("Name:",self.name)
        print("Course:",self.course)
        print("Study hourse:",self.study_hours)

student1 = Student("Gagan","CSE AI & ML",4)
student2 = Student("Sunny","CSE AI & ML",5)

student1.display_info()
print()
student2.display_info()

'''Important concepts
- __init__() — object create hone par automatically call hota hai aur uska initial data set karta hai.
- self — current object ko refer karta hai.
- Attributes — self.name, self.course jaise object ke data.
- Methods — class ke andar defined functions, jaise display_info().
Har object ka apna data hota hai. Isliye student1.name aur student2.name alag values de sakte hain.
'''