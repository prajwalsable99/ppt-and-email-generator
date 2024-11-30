 AI-Powered Email and Presentation Generator

This project leverages AI to generate customized emails and presentations. The application is built using Python with Streamlit as the front-end framework and Groq API for AI content generation.

## Features

- **Emails**: Generate personalized email templates based on user input.
- **Presentations**: Create slide presentations by selecting topics and slide types.
- **File Download**: Download generated presentations and email content directly.


main/
│
├── home.py               # Entrypoint file
├── pages/                # Folder for page scripts
│   ├── Emails.py         # Script for email generation
│   └── Presentations.py  # Script for presentation creation
│
├── .env                  # Environment variables for sensitive data like API keys
├── requirements.txt      # List of dependencies
├── output/               # Folder for generated output, e.g., screenshots
│   └── [files].jpg      # Sample screenshot files
│
├── .gitignore            # Git ignore file
└── README.md             # Readme file
