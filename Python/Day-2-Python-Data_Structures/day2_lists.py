# Lesson 1 — Python Lists
'''
A list ek aisa data structure hai jo ek variable ke andar multiple values store karta hai.
Maan le, tujhe 7 din ke study hours store karne hain.
study_hours = [2, 3, 1.5, 4, 2.5, 3, 5]

print(study_hours)
print(study_hours[0])
print(study_hours[3])

Output:
[2, 3, 1.5, 4, 2.5, 3, 5]
2
4

List ke important operations

study_hours = [2, 3, 1.5]

# Add a new value
study_hours.append(4)

# Update an existing value
study_hours[0] = 2.5

# Remove a value
study_hours.remove(3)

# Count total values
print(len(study_hours))

print(study_hours)
Output:
3
[2.5, 1.5, 4]
Dhyaan de: append() end mein value add karta hai, len() elements count karta hai aur remove() matching value ko remove karta hai.
'''