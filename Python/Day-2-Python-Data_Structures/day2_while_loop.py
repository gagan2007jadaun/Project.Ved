# Jab tak condition True rahe, loop chalta rehta hai.
'''
day = 1

while day <= 7:
    print("Day:", day)
    day += 1

Output:
Output: Day 1 se Day 7 tak print hoga.

day += 1 bahut important hai. Iske bina condition true reh sakti hai aur loop continuously chalta rahega.
'''

study_hours = [3,5,2,6,7,3.5,5.5]
total = 0
consistency_days = 0

print("====PROJECT DEV====")
print("WEEKLLY STUDY REPORT")
print()

# print daily study hours
for day, hours in enumerate(study_hours, start=1):
    print(f"Day: {day}: {hours} hours")

    # calculate total study hours
    total += hours

    if hours >= 2:
        consistency_days += 1

# calculate average study hours
average = total / len(study_hours)

# Display final report
print("\ntotal study hours: ", total)
print("average study hours: ", average)
print("Days with 3 or more than 3 hours of study: ", consistency_days)
print("Total study days: ", len(study_hours))

if consistency_days >=5:
    print("Consistency : Excellent")
elif consistency_days >= 3:
    print("Consistency : Good")
else:
    print("Consistency : Keep Improving!")
print("====END OF REPORT====")
print("====THANK YOU====")