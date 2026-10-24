# Project VED - Persistent Study Tracker

try:
    name = input("Enter your name: ")
    hours = float(input("Enter today's study hours: "))

    if not name.strip():
        print("Error: Name cannot be empty.")

    elif hours < 0:
        print("Error: Study hours cannot be negative.")

    else:
        with open("study_data.txt", "a") as file:
            file.write(f"Student: {name}\n")
            file.write(f"Study hours: {hours}\n")
            file.write("--------------------\n")

        print("Study record saved successfully!")

        with open("study_data.txt", "r") as file:
            saved_data = file.read()

        print("\n===== ALL SAVED RECORDS =====")
        print(saved_data)

except ValueError:
    print("Invalid input. Enter a numeric value for hours.")
