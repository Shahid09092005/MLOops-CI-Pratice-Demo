import streamlit as st

st.title("Mini-Calculator")
st.write("This mini-calculator will calculate the square, cube and 5th power of a given number.")

# taking input from the user 
num=st.number_input("Enter the number number")

# calculating the square, cube and 5th power of the number
sqr=num**2
cube=num**3
fifth=num**5
# displaying the results
st.write(f"the given number is {num} \n 1. Square of the number is {sqr} \n 2. Cube of the number is {cube} \n 3. 5th power of the number is {fifth}")
# st.close()