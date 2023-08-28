import streamlit as st
from constants.generate_questions_data import get_generated_questions

def generate_interview_questions():

    resume_file = st.file_uploader("Upload Candidate's Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Enter Job Description")

    # if st.button("Generate Questions"):
    #     if resume_file and job_description:
    #         files = {'resume': resume_file}
    #         data = {'job_description': job_description}
    #         response = requests.post("http://127.0.0.1:6000/generate-interview-questions", files=files, data=data)
    #         result = response.json()

    # generated_questions = []
    # st.subheader("Generated Questions:")
    # for idx, question in enumerate(generated_questions, start=1):
    #     st.write(f"{idx}. {question}")

    # Hardcoded code
    if st.button("Generate Questions"):
        if resume_file and job_description:
            questions = get_generated_questions()
            st.subheader("Generated Questions:")
            st.write(questions)