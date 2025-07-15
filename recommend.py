import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(user_skills, job_dataset_path):
    jobs_df = pd.read_csv(job_dataset_path)     

    if 'Job Title' not in jobs_df.columns or 'Skills' not in jobs_df.columns:
        raise ValueError("Dataset must contain 'Job Title' and 'Skills' columns.")
    
    jobs_df['Skills'] = jobs_df['Skills'].fillna('')  # Handle missing values
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(jobs_df['Skills'])
    user_skills_vector = tfidf_vectorizer.transform([user_skills])  
    similarity_scores = cosine_similarity(user_skills_vector, tfidf_matrix)[0]
    jobs_df['Similarity'] = similarity_scores*100
    recommended_jobs = jobs_df.sort_values(by='Similarity', ascending=False)
    recommended_jobs=jobs_df[jobs_df['Similarity']>50]
    recommended_jobs.to_csv('JOB_recommendation/recommended_jobs.csv',index=True)
    # print( "successful")


# user_skills = "python,web designing"
# job_dataset_path = "jobs.csv"  # Path to your dataset file

# recommended_jobs = recommend_jobs(user_skills, job_dataset_path)

# print("Recommended Jobs:")
# print(recommended_jobs)  # Display top recommendations


def recommend_internships(user_skills, internship_dataset_path):
    internships_df = pd.read_csv(internship_dataset_path)    

    if 'Role' not in internships_df.columns:
        raise ValueError("Dataset must contain Role columns.")
    
    internships_df['Role'] = internships_df['Role'].fillna('')  # Handle missing values
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(internships_df['Role'])
    user_skills_vector = tfidf_vectorizer.transform([user_skills]) 
    similarity_scores = cosine_similarity(user_skills_vector, tfidf_matrix)[0]
    internships_df['Similarity'] = similarity_scores*100
    recommended_internships = internships_df.sort_values(by='Similarity', ascending=False)
    recommended_internships=internships_df[internships_df['Similarity']>50]
    recommended_internships.to_csv('JOB_recommendation/recommended_internships.csv',index=True)

# recommend_internships('python','internships.csv')

def recommend_exams(user_persue, exam_dataset_path):
    exams_df = pd.read_csv(exam_dataset_path)    

    if 'after' not in exams_df.columns:
        raise ValueError("Dataset must contain 'after' column.")

    exams_df['after'] = exams_df['after'].fillna('')  # Handle missing values
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(exams_df['after'])
    user_skills_vector = tfidf_vectorizer.transform([user_persue])
    similarity_scores = cosine_similarity(user_skills_vector, tfidf_matrix)[0]
    exams_df['Similarity'] = similarity_scores*100
    recommended_exams = exams_df.sort_values(by='Similarity', ascending=False)
    recommended_exams=exams_df[exams_df['Similarity']>50]
    recommended_exams.to_csv('JOB_recommendation/recommended_exams.csv',index=True)
    # print( "successful")

# recommend_exams('12th','JOB_recommendation/exams.csv')

def recommend_courses(user_persue,user_stream, courses_dataset_path):
    courses_df = pd.read_csv(courses_dataset_path)
    if 'pursuing' not in courses_df.columns or 'stream' not in courses_df.columns:
        raise ValueError("Dataset must contain 'pursuing' and 'stream' columns.")
    courses_df['pursuing'] = courses_df['pursuing'].fillna('')
    courses_df['stream'] = courses_df['stream'].fillna('')
    # Combine the two columns into a single string for each row
    courses_df['combined'] = courses_df['pursuing'] + ' ' + courses_df['stream']
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(courses_df['combined'])
    # Combine user input similarly
    user_input = user_persue + ' ' + user_stream
    user_skills_vector = tfidf_vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_skills_vector, tfidf_matrix)[0]
    courses_df['Similarity'] = similarity_scores
    recommended_courses = courses_df.sort_values(by='Similarity', ascending=False)
    recommended_courses = recommended_courses[recommended_courses['Similarity'] > 0.1]
    recommended_courses.to_csv('JOB_recommendation/recommended_courses.csv', index=True)
    # print(courses_df['stream'])

recommend_courses("graduation","cse",'JOB_recommendation/courses.csv')