# 1. Error and exception kya hote hain?
'''
Kabhi user number ki jagah text enter kar deta hai, kabhi file nahi milti, aur kabhi calculation invalid ho sakti hai. Aise situations ko handle karne ke liye Python mein try, except, 
else aur finally use hote hain.
Example:
number = int(input("Enter a number: ))
print(number * 2)

Agar user hello enter kare, toh ValueError aayega aur programme normally stop ho jayega.
Hum ise handle kar sakte hain.
'''

# 2. try and except
try:
    num = int(input("Enter a number: "))
    result = num * 2
    print("Double:", result)

except ValueError:
    print("Error: Please enter a valid whole number.")
print("Program finished.")

'''Input 5 → output Double: 10
Input hello → error message display hoga, programme crash nahi karega.
'''

# 3. else and finally
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Inavlid input.")
else:
    print("Your number is:", num)
finally:
    print("Input process finished.")

'''
else tab run hota hai jab try block mein exception nahi aata.
finally cleanup ke liye use hota hai; exception aaye ya na aaye, ye aam taur par execute hota hai.
'''