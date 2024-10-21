# Temperature Conversion Assignment
# Pak King Lee
# Oct 17, 2024

# ask user type of conversion
start_temp = input("What temperature do you want to convert from? (C, F, or K) ")
# Foolproof
while start_temp != "C" and start_temp != "F" and start_temp != "K": 
    print("This is not a supported temperature, try again!")
    start_temp = input("What temperature do you want to convert from? (C, F, or K) ")
end_temp = input("What temperature do you want to convert to? (C, F, or K) ")
# Foolproof
while end_temp != "C" and end_temp != "F" and end_temp != "K": 
    print("This is not a supported temperature, try again!")
    end_temp = input("What temperature do you want to convert to? (C, F, or K) ")
    
#Ask user value of initial temperature
temp_value = input("How many degrees? ")
# Foolproof if temperature value not a number
while type(temp_value) == str:
    try:
        temp_value = float(temp_value)
    except ValueError:
        print("This is not a number, try again!")
        temp_value = input("How many degrees? ")

        
# convert to celsius
if start_temp == "C":
    celsius = temp_value
elif start_temp == "F":
    celsius = (temp_value - 32) * 5 / 9
elif start_temp == "K":
    celsius = temp_value - 273.15

# convert to user desired temp
if end_temp == "C":
    answer = round(celsius, 2)
    print("It is", answer, "degrees Celsius.")
elif end_temp == "F":
    answer = round(celsius * 9 / 5 + 32, 2)
    print("It is", answer, "degrees Farenheit.")
elif end_temp == "K":
    answer = round(celsius + 273.15, 2)
    print("It is", answer, "degrees Kelvin.")

# Bonus: Tell user if temperature lower than 0 degree Kelvin
if celsius < -273.15:
    print("Temperature below absolute zero, not possible.")