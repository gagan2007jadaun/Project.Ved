# Python strings
"""
String ka matlab text hota hai. Python mein strings single quotes, double quotes ya triple 
quotes mein likhi ja sakti hain.
"""
# name = "Gagan Jadaun"
# project = "Python Strings"
# print(name)
# print(project)
# print(type(name))

'''
1. String indexing
Har character ka ek index hota hai, jo 0 se start hota hai.
Example string: "VED"
V
Index 0


E
Index 1


D
Index 2
'''
# word = "VED"
# print(word[0])
# print(word[1])
# print(word[2])

'''
2. String slicing
Slicing se string ka ek portion nikal sakte hain.
'''
# project = "Python Strings"
# print(project[0:7]) # Python
# print(project[7:14])    #Strings
# print(project[:7])  # Python
# print(project[7:])  # Strings
# print(project[-1:]) # s
# print(project[:-1]) # Python String
# print(project[::-1])    # sgnirtS nohtyP
# print(project[:])   # Python Strings
# Important rule: string[start:end] mein start include hota hai, lekin end include nahi hota.

# 3. Useful string methods
message = " welcome to project ved "
print(message.upper())  #  WELCOME TO PROJECT VED 
print(message.lower())  # welcome to project ved
print(message.strip())  #welcome to ved
# strip : Beginning aur ending ke extra whitespace hataata hai
print(message.title())  # Welcome To Project Ved
#  title : har word ka first letter capital karta hai
print(message.replace("ved", "AI")) # welcome to project AI
print(message.count("e"))   # 4
'''Dhyaan rahe: ye methods generally original string ko change nahi karte; ye ek nayi string return karte hain.'''
