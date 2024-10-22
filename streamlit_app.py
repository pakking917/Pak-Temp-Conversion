import streamlit as st

st.title("🎈 Pak - Temperature Conversion")
# ask user type of conversion
start_temp = st.radio("Select the temperature you want to convert from: ", ["Celsius", "Fahrenheit", "Kelvin"])
end_temp = st.radio("Select the temperature you want to convert to: ", ["Celsius", "Fahrenheit", "Kelvin"])    
    
#Ask user value of initial temperature
temp_value = st.number_input("How many degrees? ")  

# convert to celsius
if start_temp == "Celsius":
    celsius_value = temp_value
elif start_temp == "Fahrenheit":
    celsius_value = (temp_value - 32) * 5 / 9
elif start_temp == "Kelvin":
    celsius_value = temp_value - 273.15

# convert to user desired temp
if end_temp == "Celsius":
    answer = round(celsius_value, 2)
    st.write("It is", answer, "degrees Celsius.")
elif end_temp == "Fahrenheit":
    answer = round(celsius_value * 9 / 5 + 32, 2)
    st.write("It is", answer, "degrees Farenheit.")
elif end_temp == "Kelvin":
    answer = round(celsius_value + 273.15, 2)
    st.write("It is", answer, "degrees Kelvin.")
    
# Bonus: Tell user if temperature lower than 0 degree Kelvin
if celsius_value < -273.15:
    st.write("Temperature below absolute zero, not possible in real world.")