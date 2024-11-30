import os
from dotenv import load_dotenv
from groq import Groq
import streamlit as st


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(api_key=GROQ_API_KEY)

st.set_page_config(
    page_title="Email Creation", 
    page_icon="✉️",  # Favicon for the email page

)



st.title("Email Draft Generator")

subject = st.text_input("Email Subject", "")
body_prompt = st.text_area("Email Body Prompt", "")


def generate_email(subject, body_prompt):
    try:
        # Use Groq's chat completions API for generating email content
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a professional email with the subject '{subject}' and body: {body_prompt}",
                }
            ],
            model="llama3-8b-8192",  # Choose an appropriate model
        )

        # Return the generated email
        return chat_completion.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {str(e)}"

if st.button("Generate Email Draft"):
    if subject and body_prompt:
        
        generated_email = generate_email(subject, body_prompt)

        if generated_email:
            st.subheader("Generated Email Draft:")
            st.text_area("Drafted Email", generated_email, height=300)
        else:
            st.error("Failed to generate email. Please try again.")
    else:
        st.error("Please enter both the subject and body prompt to generate the email.")
