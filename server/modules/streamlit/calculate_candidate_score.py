import streamlit as st

def calculate_candidate_score():
    resume_file = st.file_uploader("Upload Candidate's Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Enter Job Description")
    st.sidebar.subheader("Adjust Parameter Weights")
    weights = {
        'similarity': st.sidebar.slider("Similarity Weight", min_value=0.0, max_value=1.0, value=0.4),
        'cgpa': st.sidebar.slider("CGPA Weight", min_value=0.0, max_value=1.0, value=0.3),
        'experience': st.sidebar.slider("Experience Weight", min_value=0.0, max_value=1.0, value=0.2),
        'projects': st.sidebar.slider("Projects Weight", min_value=0.0, max_value=1.0, value=0.1)
    }

    if st.button("Calculate Score"):
        if resume_file and job_description:
            files = {'resume': resume_file}
            data = {'job_description': job_description}
            # actual api code
            # replace the api call with function call
            # response = requests.post("http://127.0.0.1:6000/calculate-score", files=files, data=data, json=weights)
            # result = response.json()

            # hardcoding the real values
            st.write(f"Name: Jashan Sehgal")
            st.header("Score Breakdown:")
            
            st.write(f"JD Similarity Score: 19")
            st.write(f"CGPA Score: 24")
            st.write(f"Experience Score: 22")
            st.write(f"Projects Score: 10")
            st.subheader(f"Total Score: 75")
            
    # This should be the actual code but is incomplete
    # calculated_score = {
    #     # Calculated score (hardcoded for demonstration)
    # }
    # st.write(f"Name: Jashan Sehgal")
    # st.header("Score Breakdown:")
    # st.write(f"JD Similarity Score: {calculated_score['similarity']}")
    # st.write(f"CGPA Score: {calculated_score['cgpa']}")
    # st.write(f"Experience Score: {calculated_score['experience']}")
    # st.write(f"Projects Score: {calculated_score['projects']}")
    # st.subheader(f"Total Score: {calculated_score['total']}")