try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))

    # Calculate result
    result = num1 / num2

except ValueError:
    print("Error: Please enter numeric value.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Result:", result)
finally:
    print("Calculation closed.")

'''
10 and 2 — result 5.0.

hello and 2 — numeric input error.

10 and 0 — division-by-zero error.
'''