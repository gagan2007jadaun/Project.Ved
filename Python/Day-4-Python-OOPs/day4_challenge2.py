# Day 4 - AI Researcher Inheritance Challenge
# PaRENT CLASS
class Person:
    def __init__(self, name):
        self.name= name

    def introduce(self):
        print("Name:", self.name)

# Child Class
class AIResearcher(Person):
    def __init__(self, name, research_area, model_name):
        super().__init__(name)
        self.research_area = research_area
        self.model_name = model_name
    def show_details(self):
        print("Researcher Name:", self.name)
        print("Research Area:", self.research_area)
        print("Model Name:", self.model_name)

# create an AI research object
research1 = AIResearcher(
    "GAGAN",
    "Artificial Intelligence",
    "Project VED Model"
)

# Display details
print("===== PROJECT VED RESEARCHER =====")
research1.introduce()
research1.show_details()

'''
AIResearcher(Person) — child class, parent class se inherit karti hai.

super().__init__(name) — parent class ke constructor ko call karta hai.

self.model_name — researcher ke model ka naam store karta hai.
'''