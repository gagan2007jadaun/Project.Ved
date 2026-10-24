# Final Mini-Project: Study Data Analyser
# project VED
# weekly data analyser
study_hours = []
print("====REPORT VED====")
print("WEEKLY DATA ANALYSER\n")

try:
    days = int(input("Enter the number of days you want to record study hours for (1-7): "))
    
    if days <= 0:
        print("Error: Enter atleast 1 day.")

    else:
        # collect study hours
        for day in range(1, days + 1):
            hours = float(input(f"Enter study hours for day {day}: "))
            if hours < 0:
                print("Error: Study hours cannot be negative. Please enter a valid number.")

                break

            study_hours.append(hours)
        else:
            # analyze the collected data
            total = 0
            consistency_days = 0

            for hour in study_hours:
                total += hour

                if hour >= 3:
                    consistency_days += 1
            average = total/len(study_hours)

            # Display final report
            print("\n====FINAL REPORT====")

            for day, hours in enumerate(study_hours, start=0):
                print(f"Day: {day + 1}, {hours} hours")

            print("\nTotal study hours: ", total)
            print("Average study hours: ", average)
            print("Days with 3 or more than 3 hours of study: ", consistency_days)
            print("Total study days: ", len(study_hours))

            if average >= 4:
                print("Performance: Excellent!")
            elif average >= 2:
                print("Performance: Good progress!")
            else:
                print("Performance: Keep improving!")

except ValueError:
    print("Invalid input, Please enter numeric values for hours and days.")