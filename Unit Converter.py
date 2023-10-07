# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert length from meters to feet
def meters_to_feet(meters):
    return meters * 3.28084

# Function to convert length from feet to meters
def feet_to_meters(feet):
    return feet / 3.28084

# Function to convert weight from kilograms to pounds
def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

# Function to convert weight from pounds to kilograms
def pounds_to_kilograms(pounds):
    return pounds / 2.20462

# Main function
def main():
    print("Unit Converter")
    print("1. Temperature Converter (Celsius to Fahrenheit and vice versa)")
    print("2. Length Converter (Meters to Feet and vice versa)")
    print("3. Weight Converter (Kilograms to Pounds and vice versa)")

    choice = input("Enter your choice (1/2/3): ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid choice. Please enter a valid option (1/2/3).")
        return

    if choice == 1:
        # Temperature Converter
        value = float(input("Enter temperature value: "))
        source_unit = input("Enter source unit (C/F): ").upper()
        target_unit = input("Enter target unit (C/F): ").upper()

        if source_unit == "C" and target_unit == "F":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C is equal to {result}°F.")
        elif source_unit == "F" and target_unit == "C":
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F is equal to {result}°C.")
        else:
            print("Invalid unit selection. Please choose 'C' or 'F' for Celsius or Fahrenheit.")
    
    elif choice == 2:
        # Length Converter
        value = float(input("Enter length value: "))
        source_unit = input("Enter source unit (M/F): ").upper()
        target_unit = input("Enter target unit (M/F): ").upper()

        if source_unit == "M" and target_unit == "F":
            result = meters_to_feet(value)
            print(f"{value} meters is equal to {result} feet.")
        elif source_unit == "F" and target_unit == "M":
            result = feet_to_meters(value)
            print(f"{value} feet is equal to {result} meters.")
        else:
            print("Invalid unit selection. Please choose 'M' or 'F' for meters or feet.")
    
    elif choice == 3:
        # Weight Converter
        value = float(input("Enter weight value: "))
        source_unit = input("Enter source unit (Kg/P): ").upper()
        target_unit = input("Enter target unit (Kg/P): ").upper()

        if source_unit == "KG" and target_unit == "P":
            result = kilograms_to_pounds(value)
            print(f"{value} kilograms is equal to {result} pounds.")
        elif source_unit == "P" and target_unit == "KG":
            result = pounds_to_kilograms(value)
            print(f"{value} pounds is equal to {result} kilograms.")
        else:
            print("Invalid unit selection. Please choose 'KG' or 'P' for kilograms or pounds.")
    
    else:
        print("Invalid choice. Please enter a valid option (1/2/3).")

if __name__ == "__main__":
    main()
