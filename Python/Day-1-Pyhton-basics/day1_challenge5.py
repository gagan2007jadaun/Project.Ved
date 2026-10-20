def consistency_check(study_hours):
    if study_hours >= 2:
        return "Good Consistency!"
    else:
        return "Try to increase your study hours."
result = consistency_check(float(input("Enter your Study hours: ")))
print(result)