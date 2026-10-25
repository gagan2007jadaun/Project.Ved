# Pyhton package
'''Module ek file hai; package related modules ko organise karne ka tareeka hai.
study_tracker/
</> __init__.py     Package initialisation
</> calculator.py   calculations
</> report.py       Report functions

__init__.py traditional regular package mein commonly use hota hai. Modern Python namspace package mein ye file har case mein required nahi hai.

example structure:
day-5/
|--main.py
|--study_tracker/
    |-- __init__.py
    |-- calculator.py
    |-- report.py

study_tracker/calculator.py:
def weekly_hours(daily_hours, days=7):
    return daily_hours * days

main.py:
from study_tracker.calculator import weekly_hours

print(weekly_hours(4))

Output:
28
'''

'''
Kab use karein? 
Jab project mein multiple related modules ho jaayein, unhe package mein organise karna code ko maintain karna easier banata hai.
'''
