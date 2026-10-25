def calculate_total(hours, days):
    return hours * days

def calculate_average(total, days):
    if days <= 0:
        raise ValueError("Days must be greater than zero.")
    return total / days

def performance(average):
    if average >= 4:
        return "Excellent"
    elif average >= 2:
        return "Good"
    else:
        return "Needs improvement"