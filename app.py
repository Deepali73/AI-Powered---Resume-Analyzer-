import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract sections from resume
def extract_sections(resume_text):
    contact_info = re.search(r'\b[\w.-]+@[\w.-]+\.\w+\b', resume_text)
    skills_keywords = ["Python", "Machine Learning", "NLP", "Data Analysis", "AI"]
    skills = [skill for skill in skills_keywords if skill.lower() in resume_text.lower()]
    return {
        "Contact Info": contact_info.group(0) if contact_info else "Not Found",
        "Skills": skills or "No relevant skills found"
    }

# Match resume to job description
def match_resume_to_job(resume_text, job_description):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return similarity[0][0]

# Streamlit App
def main():
    st.title("AI-Powered Resume Analyzer")
    uploaded_resume = st.file_uploader("Upload Your Resume (TXT format)", type=["txt"])
    job_description = st.text_area("Paste Job Description Here")
    
    if uploaded_resume and job_description:
        resume_text = uploaded_resume.read().decode("utf-8")
        sections = extract_sections(resume_text)
        score = match_resume_to_job(resume_text, job_description)
        
        st.subheader("Analysis Results")
        st.write(f"**Matching Score:** {score:.2f}")
        st.write("**Extracted Sections:**")
        st.json(sections)

        st.subheader("Recommendations:")
        if score < 0.5:
            st.write("Consider adding skills or keywords from the job description to your resume.")
        else:
            st.write("Your resume is well-matched to this job description!")

if __name__ == "__main__":
    main()
