import pdfplumber
import streamlit as st


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()




if __name__ == "__main__":
    with open("resumme.pdf", "rb") as f:
        resume_text = extract_text_from_pdf(f)
        print(resume_text)
