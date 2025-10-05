import streamlit as st
import random
import string
st.set_page_config(page_title="Random Password Generator", page_icon=":key:")
st.title("🔑Random Password Generator")
st.markdown("Generate a secure random password with the desired length and character types.")
length = st.slider("Select password length", min_value=8, max_value=32, value=12)
include_uppercase = st.checkbox("Include uppercase letters", value=True)
include_lowercase = st.checkbox("Include lowercase letters", value=True)
include_digits = st.checkbox("Include digits", value=True)
include_special = st.checkbox("Include special characters", value=True)
def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    if not characters:
        st.error("Please select at least one character type.")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
if password:
    st.success("Your generated password is:")
    st.code(password, language='plaintext')
    st.download_button("Download Password", password, file_name="password.txt", mime="text/plain")
