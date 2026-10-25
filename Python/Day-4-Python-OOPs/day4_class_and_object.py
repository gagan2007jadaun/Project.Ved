# class aur object kya hote hain?
'''
Maan le, humein apne Study Tracker mein 100 students ka data manage karna hai. Har student ke liye alag variables aur functions banane se code difficult ho jayega.

OOP mein hum ek class banate hain jo blueprint ki tarah kaam karti hai. Us blueprint se multiple objects bana sakte hain.

class = Blueprint = structure define karti hai
object = Actual instance = blueprint se bani specific entity'''

class Student:
    pass
student1 = Student()
student2 = Student()

print(student1)
print(student2)
'''
Output mein do alag object references dikhenge. Exact memory addresses har run mein different ho sakte hain.

Samajh: class Student: blueprint define karta hai. Student() us class ka naya object create karta hai. pass filhaal empty class ke liye placeholder hai.
'''