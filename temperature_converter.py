unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit.lower() == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp}F")
elif unit.lower() == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celcius is {temp}C")
else:
    print(f"{unit} is an invalid unit of measurment")