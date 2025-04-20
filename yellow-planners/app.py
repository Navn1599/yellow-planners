from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# --- Page Configuration ---
st.set_page_config(
    page_title="Yellow Planners by SN Catering",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Set Background Image with Transparency ---
def set_bg_image(image_path):
    # Custom CSS to set the background image with transparency on top of the background color
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #FFEB3B;  /* Background color from config */
            background-image: url({image_path});
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
            min-height: 100vh;  /* Ensures the background covers the full screen height */
            position: relative;
        }}
        .stApp::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(255, 235, 59, 0.7);  /* 30% opacity overlay */
            z-index: -1;  /* Ensures the overlay is behind the content */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with the correct image path (use the correct path for your image)
set_bg_image('file:///C:/Users/Navee/Desktop/WEBPAGE/image/wed.jpg')  # Absolute path with file://

# --- Load Lottie animation from URL ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ✅ Working JSON URL (you can replace it with another if you'd like)
lottie_coding = load_lottieurl("https://lottie.host/4c7a6fa5-b30c-43e9-b786-892054d4c643/zri4P9qmdW.json")

# --- Load image for resizing ---
img_contact_from = Image.open(r"C:\Users\Navee\Desktop\WEBPAGE\image\sn.jpg")  # Fixed path

# Resize the image by 30%
width, height = img_contact_from.size
new_width = int(width * 0.7)  # Reduce width by 30%
new_height = int(height * 0.7)  # Reduce height by 30%
img_resized = img_contact_from.resize((new_width, new_height))

# --- Content Layout ---
# Use full-screen layout with two columns (left for text, right for animation)
left_column, right_column = st.columns([2, 3])  # Adjusted ratio for larger animation side

# Left column for text
with left_column:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap');

        @keyframes smoothSlideIn {
            0% {
                opacity: 0;
                transform: translateX(-150px);
            }
            100% {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .welcome-title {
            animation: smoothSlideIn 3s ease-in-out forwards;
            font-size: 56px;
            font-family: 'Quicksand', sans-serif;
            color: #F7B733;
            text-align: left;
            margin-bottom: 0.2em;
        }

        .subtitle {
            text-align: left;
            font-size: 26px;
            color: #34495E;
            margin-top: 0;
        }

        .desc-text {
            text-align: left;
            font-size: 20px;
            color: #555;
            margin-top: 25px;
        }
        </style>

        <h1 class='welcome-title'> Welcome to Yellow Planners </h1>
        <h3 class='subtitle'>by SN Catering</h3>
        <div class='desc-text'>
            <p>Where your <b>dream events</b> become <b>delicious memories</b> 🍽</p>
            <p>Crafted with passion, delivered with perfection.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Right column for Lottie animation
with right_column:
    st.lottie(lottie_coding, height=600, key="welcome-lottie")

# --- Dish Sections in Horizontal Layout ---
st.header("Our Dishes")

# Create a row with four columns for each dish
col1, col2, col3, col4 = st.columns(4)  # Creating four equal columns

with col1:
    st.subheader("South Indian Dishes")
    south_indian_image = Image.open(r"C:\Users\Navee\Desktop\WEBPAGE\image\south indian.jpg")
    st.image(south_indian_image, caption="Authentic South Indian Dishes", width=300)
    st.write("From crispy dosas to flavorful sambar, we bring you the essence of South India with every bite.")

with col2:
    st.subheader("Chinese Dishes")
    chinese_image = Image.open(r"C:\Users\Navee\Desktop\WEBPAGE\image\chineese.jpg")
    st.image(chinese_image, caption="Delicious Chinese Dishes", width=300)
    st.write("Indulge in the finest Chinese dishes, crafted to perfection for your event.")

with col3:
    st.subheader("North Indian Dishes")
    north_indian_image = Image.open(r"C:\Users\Navee\Desktop\WEBPAGE\image\north indian.jpg")
    st.image(north_indian_image, caption="Flavorful North Indian Dishes", width=300)
    st.write("Taste the rich flavors of North India with our selection of curries and breads.")

with col4:
    st.subheader("Continental Dishes")
    continental_image = Image.open(r"C:\Users\Navee\Desktop\WEBPAGE\image\continental.jpg")
    st.image(continental_image, caption="Exquisite Continental Dishes", width=300)
    st.write("Enjoy a sophisticated selection of continental dishes, from pastas to seafood.")

# --- Contact Us Panel ---
st.header("Contact Us")

# Input Fields for user info
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

# Button to submit the form
submit_button = st.button("Send Message")

# Handling the form submission
if submit_button:
    if name and email and message:
        st.success("Thank you for your message! We will get back to you shortly.")
    else:
        st.error("Please fill in all the fields.")

# Contact Information
st.subheader("Our Contact Information")
st.write(":email: sncateringpattabiram@gmail.com")
st.write(":telephone_receiver: +91 9566012029")

# Image with text (Resized image)
with st.container():
    st.write("")  # Space before the image container
    image_column, text_column = st.columns((1, 2))

    with image_column:
        # Use the resized image and ensure the image fits the container width
        st.image(img_resized, use_container_width=True)
    with text_column:
        st.header("By SN Catering")  # Title beside the image
        st.write("Providing exceptional catering services for your special moments.")
