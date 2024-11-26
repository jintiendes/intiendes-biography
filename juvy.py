import streamlit as st
from PIL import Image  # Import for image processing
import requests  # Import for image fetching (if using URL)
from io import BytesIO

# Set page title and icon
st.set_page_config(page_title="BIOGRAPHY", page_icon=":memo:")

# Add a header
st.title("BIOGRAPHY")

# Image Section
with st.container():  # Use container for image section
    # Default image URL
    default_image_url = (
        "https://scontent.xx.fbcdn.net/v/t1.15752-9/462568097_609984578025898_6515029681787280934_n.jpg?stp=dst-jpg_p480x480&_nc_cat=101&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeGBK1dTRvCFwm5vgHC9Tno6YUCn5It7G5hhQKfki3sbmLR5MSWzWmgQ9Vkv3CWauEuRhNp1cnuv5332WKGYeH18&_nc_ohc=8LeXHlpUC5wQ7kNvgEP1jvX&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.xx&oh=03_Q7cD1QEcPo6iT0S3yZ_sSiHptJl_rI0quuKiCuZFqnk7ejVQCg&oe=676CBE55")

    # File uploader
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)
            st.image(image, caption="Profile Picture", width=400)
        except Exception as e:
            st.error(f"Error displaying the uploaded image: {e}")
    else:
        try:
            # Fetch default image from URL
            response = requests.get(default_image_url)
            response.raise_for_status()  # Raise an error for invalid responses
            default_image = Image.open(BytesIO(response.content))
            st.image(default_image, caption="Profile Picture", width=400)
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching the default image: {e}")

# Who am I? Section
st.header("Who am I?")
st.write("I am currently a first-year student taking up Computer Engineering at Surigao del Norte State University.")


# Personal Information and Contact
st.header("Personal Information")

col1, col2 = st.columns(2)

with col1:
    last_name = st.text_input("Last Name:", value="Intiendes", key="last_name_personal")
    first_name = st.text_input("First Name:", value="Juvy Grace", key="first_name_personal")
    middle_initial = st.text_input("Middle Initial:", value="Ellar", key="middle_initial_personal")
    gender = st.text_input("Gender:", value="Female", key="gender")
    age = st.number_input("Age:", min_value=0, value=19, key="age")
    address = st.text_area("Home Address:", value="Barangay Ouano, Alegria, Surigao del Norte", key="address")

with col2:
    number = st.text_input("Number:", value="+639103502532", key="number")
    email = st.text_input("Email:", value="intiendesjuvygrace@gmail.com", key="email")
    facebook = st.text_input("Facebook account:", value="Juvy Grace Intiendes", key="facebook")

# Educational Attainment
st.header("Educational Attainment")
elementary = st.text_input("Elementary:", value="Alegria Central Elementary School", key="elementary")
junior_high = st.text_input("Junior High School:", value="Alegria National High School", key="junior_high")
senior_high = st.text_input("Senior High School:", value="Alegria Stand Alone Senior High School", key="senior_high")

# Parents/Guardian
st.header("Parents/Guardian")
father_name = st.text_input("Father's Name:", value="Regie S. Intiendes", key="father_name")
mother_name = st.text_input("Mother's Name:", value="Geraldina R. Ellar", key="mother_name")
guardian_name = st.text_input("Guardian's Name:", value="Geraldina R. Ellar", key="guardian_name")

# Hobbies
st.header("Hobbies")
st.text_input("", value="Playing Guitar")
st.text_input("", value="Rubik's Cube")
st.text_input("", value="Sleeping")

