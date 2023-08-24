import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from resumeparser import ResumeParser

# # Load candidate info from JSON
# with open('./info_demo.json', 'r') as json_file:
#     data = json.load(json_file)
#     candidate = data  # Assuming the JSON structure matches the provided data

parser = ResumeParser('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')
candidate=parser.query_resume()

pdf_file = request.files['resume']
        if pdf_file and pdf_file.filename.endswith('.pdf'):
            pdf_path = os.path.join('uploads', pdf_file.filename)
            pdf_file.save(pdf_path)
            resume = parser.query_resume(pdf_path)
            return jsonify(resume)
# Define weights for different factors
weights = {
    'similarity': 0.4,
    'cgpa': 0.3,
    'experience': 0.2,
    'projects': 0.1
}

# Preprocess and tokenize the job description and candidate's information
job_description = "Fronted Web developer React"
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
job_desc_tfidf = tfidf_vectorizer.fit_transform([job_description])

# Prepare candidate's information
candidate_info = " ".join([
    candidate['basic_info']['full_name'],
    candidate['basic_info']['education_level'],
    " ".join([exp['job_title'] for exp in candidate['work_experience']]),
    " ".join([proj['project_name'] for proj in candidate['project_experience']])
])
candidate_tfidf = tfidf_vectorizer.transform([candidate_info])

# Calculate similarity score
similarity_score = cosine_similarity(job_desc_tfidf, candidate_tfidf)[0][0]

# Calculate CGPA score
cgpa_score = float(candidate['basic_info']['GPA']) / 10 * weights['cgpa']

# Calculate experience score
experience_years = int(candidate['experience_years'].split()[0])

# Calculate experience score
experience_score = experience_years * weights['experience']

# Calculate projects score
projects_score = len(candidate['project_experience']) * weights['projects']

# Calculate the final score out of 100
total_score = (similarity_score * weights['similarity'] +
               cgpa_score + experience_score + projects_score) * 100

print(f"Candidate: {candidate['basic_info']['full_name']}")
print(f"Similarity Score: {similarity_score:.2f}")
print(f"CGPA Score: {cgpa_score:.2f}")
print(f"Experience Score: {experience_score:.2f}")
print(f"Projects Score: {projects_score:.2f}")
print(f"Total Score: {total_score:.2f}")
