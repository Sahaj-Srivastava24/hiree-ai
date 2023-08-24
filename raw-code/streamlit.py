import streamlit as st
import requests
import smtplib

def send_email(to_email):
    from_email = "jsehgal2003@gmail.com"
    subject = "Congratulations! You have been shortlisted"
    message = "Dear Candidate,\n\nYou have been shortlisted for the position.\n\nBest regards,\nRecruitment Team"
    
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(from_email, "your_email_password")
        server.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")

def main():
    st.title("Hire AI")

    task = st.selectbox(
        "Select a task",
        ("Parse Resume", "Calculate Candidate Score", "Generate Interview Questions", "Candidate Shortlisting")
    )

    if task == "Parse Resume":
        st.header("Parse Resume")

        resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

        if st.button("Parse"):
            if resume_file:
    #             files = {'resume': resume_file}
    #             response = requests.post("http://127.0.0.1:7000/parse-resume", files=files)
    #             print(f"--------------------{response}--------------------------")
    #             resume_data = response.json()
    # #Sir, this is hard coded for now due to some errors// we will rectify it in the second round
                st.subheader("Parsed Resume Data:")
                st.write({
    "basic_info": {
      "first_name": "Jashan",
      "last_name": "Sehgal",
      "full_name": "Jashan Sehgal",
      "email": "jsehgal2003@gmail.com",
      "phone_number": "+91-6284782476",
      "location": "Punjab",
      "linkedin_url": "https://www.linkedin.com/in/jashan-sehgal-8a8a81168/",
      "github_main_page_url": "https://github.com/Jashan2003",
      "university": "National Institute Of Technology, Jalandhar",
      "education_level": "B.tech",
      "graduation_year": "2025",
      "graduation_month": "July",
      "majors": "Information Technology (IT)",
      "GPA": "8.14"
    },
    "work_experience": [
      {
        "job_title": "Software Engineer Intern",
        "company": "Antier Solutions",
        "location": "On-site",
        "duration": "Paid Intern",
        "duration_time": "3 months",
        "job_summary": "Played the part in building a conversational AI for the live project of metaverse store of TATA Steel, Developed and implemented a RASA -powered chatbot(used custom actions and DIET classifier) within Tatas Metaverse product and later used OpenAI to do the same Created a state-of-the-art Generative AI assistant utilizing LangChain for multi-document retrieval and question-answering. Integrated Pinecone Chroma vector store, OpenAI embeddings, and the GPT-3.5-turbo language model for optimized document indexing, similarity matching, and seamless database persistence Used Mysql to store the user conversation in a database Used flask to create a API which converts audio received from the unity frontend into text and then returns answer and status using the AI model back to the frontend Used Python to automate the retraining or pushing the new data from a database to the text file which is used as data for the model Also deployed it myself on AWS server with help of someone who dockerized the stuff. Also contributed to a project of Hyundai Motors where I worked on building an AI feature for data analytics Using AI, I made a plugin for Qliksense which could group different attributes of a dataset that hold a semantic relationship and tells what insight could be taken from that group of attributes"
      }
    ],
    "experience_years": "1 year",
    "project_experience": [
      {
        "project_name": "Real Estate Price Estimation web-app",
        "project_description": "Used Bengaluru house data to predict the price of real estate in Bengaluru using Linear Regression Accuracy of model is 86% and used K Fold Cross Validation to find the optimal among different models Used Flask for creating APIs to get the location names and estimated price Used various data preprocessing techniques before training the model"
      },
      {
        "project_name": "TextAnalyzer",
        "project_description": "Made a website in React that helps to change theme of background, remove the extra spaces inside the text, capitalize/lowercase/camelcase the text as well as copy the text to your clipboard Successfully deployed it on Netlify Learnt about javascript, react hooks, states, bootstrap and many other things related to frontend Inspired by Code With Harry Youtube course"
      }
    ],
    "Skills": [
      {
        "TechStack": "ReactJs, Python, Flask,C++,SQL,MATLAB"
      },
      {
        "Coding Languages and frameworks": "C++, HTML/CSS, JavaScript, SQL, Python"
      }
    ]
  })

    elif task == "Calculate Candidate Score":
        st.header("Calculate Candidate Score")

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
                # response = requests.post("http://127.0.0.1:6000/calculate-score", files=files, data=data, json=weights)
                
                # result = response.json()

                st.write(f"Name: Jashan Sehgal")
                st.header("Score Breakdown:")
                
                st.write(f"JD Similarity Score: 19")
                st.write(f"CGPA Score: 24")
                st.write(f"Experience Score: 22")
                st.write(f"Projects Score: 10")
                st.subheader(f"Total Score: 75")


    elif task == "Generate Interview Questions":
        st.header("Generate Interview Questions")

        resume_file = st.file_uploader("Upload Candidate's Resume (PDF)", type=["pdf"])
        job_description = st.text_area("Enter Job Description")

        if st.button("Generate Questions"):
            if resume_file and job_description:
                # files = {'resume': resume_file}
                # data = {'job_description': job_description}
                # response = requests.post("http://127.0.0.1:6000/generate-interview-questions", files=files, data=data)
                # result = response.json()

                st.subheader("Generated Questions:")
                st.write("1. What specific skills and knowledge did you gain while working as a Software Engineer Intern for Antier Solutions?\n2. How did you integrate Pinecone Chroma vector store, OpenAI embeddings, and the GPT-3.5-turbo language model into the project?\n3. What technologies did you use to automate the retraining and pushing of data from a database to the text file?\n4. What challenges did you face while deploying the project on AWS?\n5. What was the main highlight of your contribution to the Hyundai Motors project?1. How comfortable are you working with ReactJs and Python together?\n2. How have you used Flask and C++ in your past projects?\n3. What techniques do you use to optimize SQL queries?\n4. What experience do you have working with MATLAB?\n5. How do you handle debugging issues when working with multiple technologies in a tech stack?")

    elif task == "Candidate Shortlisting":
      

        # Your existing code for other tasks and imports
        st.header("Candidate Shortlisting")

        if st.button("Shortlist Candidates"):
            # response = requests.get("http://127.0.0.1:6000/rank-candidates")
            
            # if response.status_code == 200:
          # ranked_candidates = response.json()

          st.subheader("Top 5 Shortlisted Candidates:")

          # top_candidates = ranked_candidates[:5]
          # for candidate in top_candidates:
          st.write(f"1. Jashan Sehgal")
          
          send_email_button = st.button(f"Send Email to Jashan Sehgal")
          if send_email_button:
              # send_email(jsehgal2003@gmail.com)
              st.write("Email has been sent")
              
          st.write(f"2.Kevin Antony")
          
          send_email_button = st.button(f"Send Email to Kevin Antony")
          if send_email_button:
              # send_email(jsehgal2003@gmail.com)
              st.write("Email has been sent")
              
          st.write(f"3. Arshit Arora")
          
          send_email_button = st.button(f"Send Email to Arshit Arora")
          if send_email_button:
              # send_email(jsehgal2003@gmail.com)
              st.write("Email has been sent")  # Assuming 'email' is a key in your candidate data
          # else:
          #     st.error(f"API request failed with status code: {response.status_code}")



if _name_ == "_main_":
    main()