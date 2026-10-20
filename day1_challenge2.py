try:
    study_hours=float(input("Enter your Study hours: "))
    print("Your total study hours:", study_hours)
    if study_hours < 0:
        print("Study hours cannot be negative. Please enter a valid number.")
    elif study_hours == 0:
        print("You haven't studied at all. Please try to study more.")
    else:
        print("Valid study hours:", study_hours)
except ValueError:
    print("Invalid input! Please enter a valid number for study hours.")