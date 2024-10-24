'''
Author: Ashutosh Devpura
Email: ashutoshdevpura@gmail.com
'''

import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

# Load environment variables'
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini response with specific model configuration
def get_gemini_response(input):
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        generation_config={"response_mime_type": "application/json"}
    )
    response = model.generate_content(input)
    return response.text

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = pdf.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Updated prompt to ask for keyword categorization
input_prompt = """
    You are an advanced ATS system integrated with LLM capabilities, specializing in reviewing tech resumes.
    Given a resume and job description, you will:
    1. Analyze the resume's alignment with the job description.
    2. Provide a score out of 100 based on the match.
    3. Categorize the missing keywords into the following groups:
        - Programming Languages
        - Tools and Software
        - Algorithms
        - Frameworks
        - Others (if applicable)
    Provide the result in JSON format as follows:
    {{"score": score, 
    "categorized_keywords": {{
        "Programming Languages": [list of programming languages], 
        "Tools and Software": [list of tools and software], 
        "Algorithms": [list of algorithms], 
        "Frameworks": [list of frameworks], 
        "Others": [list of other missing keywords]
    }}
    }}
"""

# Streamlit App with Dark Theme
st.set_page_config(page_title="ATS Resume Analyzer", page_icon=":robot_face:", layout="centered")

# Custom CSS to enhance technical feel with a dark theme
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
            color: #f5f5f5;
        }
        .reportview-container {
            background: #1e1e1e;
            color: #f5f5f5;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #f5f5f5;
        }
        .sidebar .sidebar-content {
            background: #222;
            color: #fff;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
        }
        .stTextInput > div > input {
            background-color: #222;
            color: #f5f5f5;
        }
        .stFileUploader label {
            color: #f5f5f5;
        }
    </style>
""", unsafe_allow_html=True)

# Header section with tech-oriented feel
st.title("🔍 LLM GenAI Powered ATS Resume Analyzer")
st.markdown("""
    **Welcome to the ATS Resume Checker!**  
    Leverage the power of *Large Language Models (LLM)* and *Generative AI (GenAI)* to review your resume based on specific job descriptions.  
    Get a score out of 100 and discover which keywords are missing to make your resume ATS-compliant for tech jobs!
""")

# Job description input with a technical edge
st.subheader("🛠️ Input Job Description")
st.markdown("""
    Paste the **Job Description** you'd like to optimize your resume for:
""")
job_description = st.text_area("Job Description:", help="Paste the job description here.")

# Resume upload section with a more technical feel
st.subheader("📄 Upload Your Resume")
uploaded_file = st.file_uploader("Upload your resume in **PDF format**. The system will extract text from the file, analyze it using LLM-powered AI, and provide feedback on how well it aligns with the job description.", type="pdf", help="Upload the resume file.")

# Submit button with progress indicator
submit = st.button("Analyze Resume 🔍")

if submit:
    if uploaded_file is not None and job_description:
        st.info("⚙️ Processing... Analyzing resume using Generative AI.")
        progress_bar = st.progress(0)  # Adding a progress bar to indicate loading

        resume_text = extract_text_from_pdf(uploaded_file)
        input_text = input_prompt.format(text=resume_text, job_description=job_description)
        
        # Simulate analysis progress
        for percent_complete in range(0, 101, 10):
            progress_bar.progress(percent_complete)
        
        response = get_gemini_response(input_text)
        st.success("✅ Analysis Complete!")
        
        # Parsing the response (assuming it's returned as a string in JSON format)
        response_data = eval(response)  # Convert the response string into a dictionary
        categorized_keywords = response_data["categorized_keywords"]
        
        # Display categorized output
        st.subheader("📊 Categorized Missing Keywords")
        st.markdown("Here’s how your resume stacks up against the job description:")

        for category, keywords in categorized_keywords.items():
            if keywords:
                st.markdown(f"**{category}:** {', '.join(keywords)}")
        
        st.subheader("🔢 ATS Score")
        st.text(f"Your score is: {response_data['score']} / 100")

    elif not uploaded_file:
        st.error("⚠️ Please upload a PDF resume file.")
    elif not job_description:
        st.error("⚠️ Please provide the job description.")

# Footer with a technical signature
st.markdown("""
    ---
    **Made with ❤️ by [Ashutosh Devpura](mailto:ashutoshdevpura@gmail.com)**  
    Powered by **Google Generative AI** | Streamlit 
""")
