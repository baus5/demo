"""
    Temperature Formulas,

    Note:
    In general, temperature values are rounded to the nearest whole number for display purposes.

    Standard Rounding (.5 rule):
    If the decimal is .5 or higher, it rounds up. If it is less than .5, it rounds down.
    
    Example: 22.5°C becomes 23°C.
    Example: 72.4°F becomes 72°F.

    Note2:
    Python 3 uses "Banker's Rounding," meaning values ending in .5 round to the nearest even integer.

    print(round(4.6)) # Output: 5
    print(round(4.4)) # Output: 4
    print(round(2.5)) # Output: 2 (even)
    print(round(3.5)) # Output: 4 (even)
"""

import sys

print("Enter Fahrenheit or Press [Return] to Celsius:")
user_input = input("> ")

if user_input == "":
    print("Enter Celsius:")
    user_input = input("> ")

    # Terminate the script immediately
    if user_input == "":
        sys.exit()

    C = int(user_input)

    # from Celsius(C) to Fahrenheit(F) formula
    F = (9 / 5 * C) + 32
    print(round(F), "F degree")
else:
    # Fahrenheit
    F = int(user_input)

    # from Fahrenheit(F) to Celsius(C) formula
    C = 5 / 9 * (F - 32)
    print(round(C), "C degree")
