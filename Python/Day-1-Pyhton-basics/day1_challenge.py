name=input("Enter your name: ")
study_hours=float(input("Enter your Study hours: "))
month=int(input("Enter total days of current month "))
total_study_hours=study_hours * month
# print("total study hours in month is ",total_study_hours)
if month>=1 and month<=31:
    print("Total study hours in this month is ",total_study_hours)
    if study_hours>=2:
        print("Good Consistency!")
    else:
        print("Try to increase your study hours.")
else:
    print("Maybe, invalid date you enter!")