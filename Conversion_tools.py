# --- Convert Miles to Kilometers ---
def miles_to_kilometers(miles):
    return miles * 1.609344

try:
    miles = float(input("Enter distance in miles: "))
    kilometers = miles_to_kilometers(miles)
    print(f"{miles} miles is equal to {kilometers:.4f} kilometers.\n")
except ValueError:
    print("Invalid input! Please enter a valid number.\n")


# --- Convert Decimal to Binary ---
def dec_to_binary(n):
    if n == 0:
        return "0"
    negative = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    binary_str = ''.join(reversed(bits))
    return "-" + binary_str if negative else binary_str

try:
    num = int(input("Enter a decimal number: "))
    binary = dec_to_binary(num)
    print(f"Binary representation: {binary}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


#Temperature
print('Temperature Conversion Program')
print('Selections:::\nPress 1 for Celsius\nPress 2 for Fahrenheit\nPress 3 for Kelvin')

try:
    choice = int(input('Enter your selection: '))
    
    if choice == 1: 
        # Celsius conversions
        temp = float(input('Enter temperature in Celsius: '))
        fahrenheit = (9/5) * temp + 32
        kelvin = temp + 273.15
        print(f'Fahrenheit: {round(fahrenheit, 2)}°F')
        print(f'Kelvin: {round(kelvin, 2)}K')
    
    elif choice == 2: 
        # Fahrenheit conversions
        temp = float(input('Enter temperature in Fahrenheit: '))
        celsius = (temp - 32) * 5/9
        kelvin = (temp - 32) * 5/9 + 273.15  # Verified formula
        print(f'Celsius: {round(celsius, 2)}°C')
        print(f'Kelvin: {round(kelvin, 2)}K')
    
    elif choice == 3:
        # Kelvin conversions
        temp = float(input('Enter temperature in Kelvin: '))
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * 9/5 + 32  # Verified formula
        print(f'Celsius: {round(celsius, 2)}°C')
        print(f'Fahrenheit: {round(fahrenheit, 2)}°F')
    
    else:
        print('Invalid Option! Please choose 1, 2, or 3.')

except ValueError:
    print('Error: Please enter valid numbers only!')