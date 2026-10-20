def calculate_study_hours(daily_hours, days):
    return daily_hours * days

def consistency_check(study_hours):
    if study_hours >= 2:
        return "Good Consistency"
    else:
        return "Try to increase your study hours"

try:
    name = input("Enter your name: ")
    daily_hours = float(input("enter the number of hours you study daily: "))
    days = int(input("enter the number of days you study in this month: "))

    if daily_hours < 0:
        print("Daily study hours cannot be negative.")
    elif days <1 or days > 31:
        print("Number of days should be between 1 and 31.")
    else:
        total_study_hours = calculate_study_hours(daily_hours, days)
        message = consistency_check(daily_hours)
        print("\nHello,",name)
        print("Total study hours in this month:", total_study_hours)
        print(message)
except ValueError:
    print("Invalid input, Please enter numeric values for hours and days.")