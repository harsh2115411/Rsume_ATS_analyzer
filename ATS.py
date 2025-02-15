import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = "".join(page.extract_text() or "" for page in reader.pages)
    return text  # Limit characters sent to AI


def calculate_jd_match(resume_text, jd_text): # calculate the ATS score using TF-IDF cosine similarity 
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return round(similarity * 100, 2)


def find_missing_skills(resume_text, jd_text):
    jd_words = set(jd_text.lower().split())
    resume_words = set(resume_text.lower().split())
    return list(jd_words - resume_words)  # Direct set difference



def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    
    
    # Extract JSON from response
    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
    if json_match:
        response_text = json_match.group(0)
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            st.error("Error parsing AI response. Invalid JSON format.")
            return None
    else:
        st.error("Invalid AI response format.")
        return None

# Streamlit UI
with st.sidebar:
    st.title("Smart ATS for Resumes")
    st.subheader("About")
    st.write("An advanced ATS using Gemini Pro and AI-powered analysis for resume optimization.")
    st.write("--> By Harsh Pilania")

st.title("Smart Application Tracking System")
st.text("Improve Your Resume ATS Match Score")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload a PDF file.")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and jd:
        resume_text = input_pdf_text(uploaded_file)
        jd_match = calculate_jd_match(resume_text, jd)
        missing_skills = find_missing_skills(resume_text, jd)
        
        
        input_prompt = f"""
        Hey, act as an expert ATS. Analyze the resume based on the given job description.
        Generate a detailed profile summary that accurately reflects the resume's content,
        highlighting relevant experience, skills, and areas of expertise.
        
        Resume: {resume_text}
        Job Description: {jd}
        
        Response format (strict JSON, ensure valid JSON syntax):
        ```json
        {{
            "Profile Summary": "Summarize the candidate's experience based on the resume."
        }}
        ```
        If you cannot return valid JSON, output only the JSON block inside triple backticks.
        """
        response = get_gemini_response(input_prompt)
        
        if response:
            st.subheader("ATS Analysis Results")
            st.write(f"**ATS Score** {jd_match}%")
            st.write(f"**Missing Keywords:** {', '.join(missing_skills)}")
            st.write(f"**Profile Summary:** {response.get('Profile Summary', 'N/A')}")
    else:
        st.error("Please upload a resume and enter a job description.")
