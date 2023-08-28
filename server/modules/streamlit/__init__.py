import streamlit as st
from . import parse_resume, calculate_candidate_score, candidate_shortlisting, generate_interview_questions

def main():
    st.title("Hire AI")

    task = st.selectbox(
        "Select a task",
        ("Parse Resume", "Calculate Candidate Score", "Generate Interview Questions", "Candidate Shortlisting")
    )

    if task == "Parse Resume":
        st.header("Parse Resume")
        parse_resume()

    elif task == "Calculate Candidate Score":
        st.header("Calculate Candidate Score")
        calculate_candidate_score()

    elif task == "Generate Interview Questions":
        st.header("Generate Interview Questions")
        generate_interview_questions()

    elif task == "Candidate Shortlisting":
        st.header("Candidate Shortlisting")
        candidate_shortlisting()

if __name__ == '__main__':
    main()
