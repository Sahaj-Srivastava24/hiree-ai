import streamlit as st
import requests
from utils.send_email import send_email


def candidate_shortlisting():
    shortlisted_candidates = []
    st.subheader("Top 5 Shortlisted Candidates:")
    
    # for idx, candidate in enumerate(shortlisted_candidates, start=1):
    #     st.write(f"{idx}. {candidate['name']}")
    #     send_email_button = st.button(f"Send Email to {candidate['name']}")
    #     if send_email_button:
    #         # Placeholder for email sending logic (to be implemented)
    #         st.write("Email has been sent")


    if st.button("Shortlist Candidates"):
        response = requests.get("http://127.0.0.1:6000/rank-candidates")
        if response.status_code == 200:
            ranked_candidates = response.json()
            st.subheader("Top 5 Shortlisted Candidates:")

            # Assuming 'email' is a key in your candidate data for send_email()
            top_candidates = ranked_candidates[:5]
            for index, candidate in enumerate(top_candidates, start=1):
                st.write(f"{index}. {candidate}")
                send_email_button = st.button(f"Send Email to {candidate}")
                if send_email_button:
                    send_email(candidate.lower().replace(" ", "") + "@gmail.com")
                    st.write("Email has been sent")
        else:
            st.error(f"API request failed with status code: {response.status_code}")
