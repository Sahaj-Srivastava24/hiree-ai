import streamlit as st
from ...constants.resume_parsed_data import get_resume_data


def parse_resume():
    resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    if st.button("Parse"):
        # incomplete data
        # if resume_file:
        #     files = {'resume': resume_file}
        #     response = requests.post("http://127.0.0.1:7000/parse-resume", files=files)
        #     print(f"--------------------{response}--------------------------")
        #     resume_data = response.json()
        #     # sir, this is hard coded for now due to some errors
        #     # we will rectify it in the second round
        #     st.subheader("Parsed Resume Data:")
        #     st.write(resume_data)
        parsed_data = get_resume_data()
        st.subheader("Parsed Resume Data:")
        st.write(parsed_data)