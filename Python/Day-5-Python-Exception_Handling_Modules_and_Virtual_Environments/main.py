from study_tracker.calculator import(
    calculate_total,
    calculate_average,
    performance
)
try:
    hours = float(input("Enter daily study hours: "))
    days = int(input("Enter number of days: "))

    if hours < 0 or days <= 0:
        raise ValueError("Hours cannot be negative and days must be positive.")

    total = calculate_total(hours, days)
    average = calculate_average(total, days)

    print("total study hours:",total)
    print('average study hours:',round(average,2))
    print("Performance:",performance(average))

except ValueError as error:
    print("Input error:", error)