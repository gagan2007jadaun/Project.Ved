try:

    name= input("Enter your name: ")
    daily_study_hours = float(input("Enter your daily study hours: "))
    study_days = int(input("Enter total days of current month: "))
    if daily_study_hours < 0:
        print("study hours cannot be negative. Please enter a valid number.")
    elif study_days < 1 or study_days >31:
        print("Invalid number of days. Please enter a value between 1 and 31.")
    else:
        total_study_hours = daily_study_hours * study_days
        print("Hello", name)
        print("Total study hours in this month is: ", total_study_hours)

        if daily_study_hours >= 2:
            print("Good consistency! Keep up the good work.")
        else:
            print("Try to increase your study hours for better results.")

except ValueError:
    print("Invalid input! Please enter the correct datatype.")