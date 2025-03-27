import streamlit as st
import string
import random

def generate_password(length):
    if length < 8:
        return "Password length must be at least 8 characters."
    
    digit = string.digits
    symbols = string.punctuation
    lower_Alphabets = string.ascii_lowercase
    upper_Alphabets = string.ascii_uppercase
    total = digit + symbols + lower_Alphabets + upper_Alphabets
    
    temp = ''
    temp += random.choice(digit)
    temp += random.choice(symbols)
    temp += random.choice(lower_Alphabets)
    temp += random.choice(upper_Alphabets)
    
    for _ in range(length - 4):
        temp += random.choice(total)
    
    temp = list(temp)
    random.shuffle(temp)
    
    return "".join(temp)

# Streamlit UI
st.title("🔑 Random Password Generator")
st.write("Generate a secure password with a mix of letters, numbers, and symbols.")

length = st.number_input("Enter the length of the password (Min: 8)", min_value=8, value=12, step=1)

if st.button("Generate Password"):
    password = generate_password(length)
    st.success(f"Your generated password: `{password}`")
