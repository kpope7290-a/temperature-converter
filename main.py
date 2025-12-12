# main.py

import conversions

choice = input("Type 'c' to convert Fahrenheit → Celsius, or 'f' to convert Celsius → Fahrenheit: ").lower()

if choice == 'c':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = conversions.celsius(f)
    print(f"{f:.2f}°F is {c:.2f}°C")

elif choice == 'f':
    c = float(input("Enter temperature in Celsius: "))
    f = conversions.fahrenheit(c)
    print(f"{c:.2f}°C is {f:.2f}°F")

else:
    print("Invalid choice. Please type 'c' or 'f'.")
