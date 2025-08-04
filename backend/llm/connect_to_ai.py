from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_resume(resume_text, job_text):
    prompt = f"""
YYou are a career agent. First, extract the key requirements from the job description below. Then compare the resume and do the following:

1. List clearly matched skills and qualifications, if none is matching make sure to say not matching.
2. Identify important missing skills or keywords the candidate should add to the resume.
3. Suggest 3 improved bullet points the candidate could add or rewrite in their resume for this job.
4. If nothing in the resume matches the job, say 'No Match' and explain what the candidate should study or include.
5. Point out any formatting problems that would affect Applicant Tracking Systems (ATS).
6- translate to somali language

Job Description:
{job_text}

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content