def calculate_total(hours_per_day, days):
    total = hours_per_day * days
    return total
def calculate_average(total, days):
    average = total / days
    return average
def check_performance(average):
    if average >= 4:
        return "Excellent"
    elif average >= 2:
        return "Good"
    else:
        return "Needs Improvement"


# total = calculate_total(3, 7)
# average = calculate_average(total, 7)
# performance = check_performance(average)

# print("Total hours:", total)
# print("Average hours:", average)
# print("Performance:", performance)

try:
    hours_per_day = float(input("Enter daily study hours: "))
    days = int(input("Enter number of study days: "))
    if hours_per_day < 0 or days <=0:
        print("Error: hours be negative and must be positive.")
    else:
        total = calculate_total(hours_per_day, days)
        average = calculate_average(total, days)
        performance = check_performance(average)

        print("Total study hours: ", total)
        print("Average hours: ", round(average, 2))
        print("Performance: ", performance)

except ValueError:
    print("Invalid input! Please enter numeric values.")