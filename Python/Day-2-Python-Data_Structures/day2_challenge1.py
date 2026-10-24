study_hours = [2,2.5,2,3,4,5,6]
print("Daily study hours in this week:", study_hours)

# 1. accessing day 1 study hours
print("first day study hours:", study_hours[0])
# 2.accessing day 5 study hours
print("fifth day study hours:", study_hours[4])
# 3. Add 4.5 hours for a new study session
study_hours.append(4.5)
print("study_hours after adding new study session:", study_hours)
# 4. Update the first day's hours to 2.5
study_hours[0]=9.5
print("study hours after updating first day hours:", study_hours)
# 5. Print the total number of entries
print("Total number of entries:", len(study_hours))