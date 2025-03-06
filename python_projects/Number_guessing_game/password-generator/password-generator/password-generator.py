import streamlit as st
import random
import string

# Function to generate a strong password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include uppercase & lowercase letters

    if use_digits:
        characters += string.digits  # Add numbers (0-9) if selected
    if use_special:
        characters += string.punctuation  # Add special characters

    return "".join(random.choice(characters) for _ in range(length))

# Function to check password strength
def password_strength(password):
    strength = 0
    if any(c.islower() for c in password): strength += 1
    if any(c.isupper() for c in password): strength += 1
    if any(c.isdigit() for c in password): strength += 1
    if any(c in string.punctuation for c in password): strength += 1

    if strength == 1:
        return "Weak 🔴"
    elif strength == 2:
        return "Moderate 🟡"
    elif strength == 3:
        return "Strong 🟢"
    else:
        return "Very Strong 💪"

# Streamlit UI setup
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")
st.title("🔒 Secure Password Generator")

st.write("Create a strong password with customizable options.")

# User input for password length
length = st.slider("Select Password Length:", min_value=6, max_value=32, value=12)

# Checkbox options for including numbers and special characters
use_digits = st.checkbox("Include Numbers (0-9)")
use_special = st.checkbox("Include Special Characters (!@#$%^&*)")

# Generate password button
if st.button("🔄 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"**Your Secure Password:** `{password}`")
    
    # Display password strength
    st.markdown(f"**Password Strength:** {password_strength(password)}")

    # Add copy-to-clipboard functionality
    st.code(password, language="text")
