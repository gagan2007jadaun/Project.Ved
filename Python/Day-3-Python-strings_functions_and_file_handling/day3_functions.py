# Python functions
'''
print("Name starts with G:", name.startswith("G"))
print("Name ends with n:", name.endswith("n"))
print("Name without spaces:", name.replace(" ", ""))

Input: Daily hours = 3


calculate_weekly_hours()
Daily hours × 7


Output: 21 hours
'''
# def calculate_weekly_hours(daily_hours):
#     total = daily_hours * 7
#     return total
# result = calculate_weekly_hours(3)
# print("Weekly study hours: ",result)
'''
def — function define karne ke liye.
calculate_weekly_hours — function ka naam.
daily_hours — parameter, jisme input receive hota hai.
return — calculated result caller ko wapas deta hai.
calculate_weekly_hours(3) — function ko 3 argument ke saath call karta hai.
'''

# Parameters aur arguments mein difference
# def greet(name): # name = parameter
#     print("Hello,",name)
# greet("Gagan")  # "Gagan" = argument
# greet("Rahul") 
'''Ek hi function ko alag-alag inputs ke saath reuse kar sakte hain.'''

# return vs print
# print()
def add(a,b):
    print(a+b)
add(2,3)

# return
def add(a,b):
    return a+b
result = add(2,3)
print(result*2)
'''Rule: Jab calculated value ko aage kisi aur calculation mein use karna ho, toh usually return use karo.'''

# Multiple parameters aur conditions
def consistency_check(study_hours):
    if study_hours >= 3:
        return "Good Consistency!"
    else:
        return "Try to improve your Consistency."
print(consistency_check(4))
print(consistency_check(2))
'''Function ke andar if-else bhi use kar sakte hain.'''
