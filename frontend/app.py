import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import sys
import os
BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
sys.path.insert(0, BACKEND_PATH)


from utils.extract import extract_text_from_pdf
from llm.connect_to_ai import analyze_resume

st.set_page_config(page_title="SmartResume AI", layout="centered")

st.title(" SmartResume AI – Resume Analyzer")
st.write("Upload your resume and paste a job description. Get instant AI suggestions using DeepSeek.")

# 1. Resume upload
uploaded_file = st.file_uploader("upload your resume make sure it is PDF", type=["pdf"])

# 2. Job description input
job_desc = st.text_area("Paste the job description", height=250)

# 3. When both inputs are ready:
if uploaded_file and job_desc:
    # Extract resume text
    resume_text = extract_text_from_pdf(uploaded_file)

    # Show extracted resume
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=300)

    # Call DeepSeek
    st.subheader("Suggestions:")
    with st.spinner("Analyzing your resume..."):
        result = analyze_resume(resume_text, job_desc)

    # Display LLM output
    st.text_area("Output", result, height=300)

elif uploaded_file and not job_desc:
    st.warning("Please paste the job description to analyze.")

elif job_desc and not uploaded_file:
    st.warning("Please upload your resume (PDF).")
