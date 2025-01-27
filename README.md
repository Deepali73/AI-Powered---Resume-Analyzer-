# AI-Powered - Resume-Analyzer
Overview-->
The AI-Powered Resume Analyzer is a Streamlit-based web application that helps job seekers evaluate how well their resumes match a given job description. It extracts key sections from the resume, analyzes relevant skills, and calculates a matching score using TF-IDF & Cosine Similarity.

Key Features -->

1.Resume Section Extraction:-
Identifies contact information (email).
Extracts relevant skills based on predefined keywords.
2.Resume & Job Description Matching:-
Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical form.
Applies Cosine Similarity to compare the resume with the job description.
Outputs a matching score (0-1) indicating how well the resume fits the job.
3.Recommendations:-
If the match score is low (<0.5), the app suggests adding relevant skills or keywords.
If the match score is high (≥0.5), it confirms that the resume aligns well with the job description.
4.User-Friendly Interface:-
Built with Streamlit, allowing an interactive experience.
Supports file uploads for resumes in .txt format.
Provides structured JSON output for extracted sections.

Install the required python libraries -->
pip install streamlit scikit-learn

Run the Streamlit app -->
After saving the script, navigate to the folder where app.py is located and run:
streamlit run app.py
This will start a local web server, and you will see a URL in the terminal, such as:
Local URL: http://localhost:8501  

