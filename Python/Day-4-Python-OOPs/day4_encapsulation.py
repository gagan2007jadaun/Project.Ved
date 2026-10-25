# Encapsulation
'''Encapsulation ka matlab hai data aur us data par kaam karne wale methods ko ek class mein organise karna, aur zaroorat ke according access ko control karna.

Example: maan le Project VED mein ek model-training system hai. Uska learning rate koi bhi invalid value se change na kar sake.
'''

# Python mein public, protected aur private conventions
'''1. Public - name = class ke bhar se normally access kiya ja sakta hai.
self.name = "Gagan"

2. Protected convention - _name = Underscore signal karta hai ki attribute internal use ke liye intended hai. Ye strict restriction nahi hai.
self._learning_rate = 0.01

3. Name-mangled convention - __name = Double underscore Python mein name mangling activate karta hai, jisse accidental access aur overriding ka risk kam hota hai. Ye absolute security nahi hai.
self.__learning_rate = 0.01
'''
class ModelConfig:
    def __init__(self, model_name, learning_rate):
        self.model_name = model_name
        self.__learning_rate = learning_rate

    def get_learning_rate(self):
        return self.__learning_rate

    def set_learning_rate(self, new_rate):
        if 0 < new_rate <= 1:
            self.__learning_rate = new_rate
            print("Learning rate updated successfully!")
        else:
            print("Error: Learning rate must be between 0 and 1.")
    def  show_config(self):
        print("Model:", self.model_name)
        print("Learning rate:", self.__learning_rate)

#Create on object 
model = ModelConfig("VED-LM", 0.01)

model.show_config()
print("\n Current learning rate:", model.get_learning_rate())

# Update with a valid value
model.set_learning_rate(0.05)
model.show_config()

# Try an invlid value
model.set_learning_rate(5)

'''
- self.__learning_rate ek double-underscore attribute hai.
- get_learning_rate() current value return karta hai.
- set_learning_rate() pehle input validate karta hai, phir valid value update karta hai.
- 5 reject hota hai kyunki woh allowed range ke bahar hai.
Important: Python mein double underscore attribute ko bhi determined code name-mangled form ke through access kar sakta hai. Isliye ise security boundary mat samajhna. Yahan iska purpose controlled access aur accidental modification se bachav hai.
'''