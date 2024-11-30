import streamlit as st

# Set page configuration for the main page
st.set_page_config(
    page_title="ProductivityHub",
    page_icon="🏠",  # Home icon for the homepage
    initial_sidebar_state="expanded"
)

# Title for the homepage
st.title("Welcome to ProductivityHub !")

# Description of the app's features
st.markdown("""
This app is a collection of tools to help you create and organize your work:

1. **Email Creation**: Quickly generate customized emails.
2. **PowerPoint Creation**: Easily create PowerPoint presentations.


Use the sidebar to navigate to different pages and start using the features!
""")

# Add an image or other elements to make the homepage more engaging
st.image("https://cdn.pixabay.com/photo/2020/11/17/13/22/student-5752322_1280.png", caption="dont stress",width=400)



