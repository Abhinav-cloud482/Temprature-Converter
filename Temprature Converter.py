unit = input("Is this temperature in (C)elsius or (F)ahrenheit? ")
temp = float(input("Enter the temperature: "))

if unit.upper() == "C":
    temp = (temp * 9/5) + 32  # Convert to Fahrenheit
    print(f"The temperature in Fahrenheit is {temp:.1f}°F.")
elif unit.upper() == "F":
    temp = (temp - 32) * 5/9  # Convert to Celsius
    print(f"The temperature in Celsius is {temp:.1f}°C.")
else:
    print("Invalid unit")
