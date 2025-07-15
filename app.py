
from flask import Flask, render_template, request, jsonify
import csv
import os
# import subprocess
from recommend import recommend_jobs,recommend_internships,recommend_exams,recommend_courses



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/process', methods=['POST'])
def process():
    user_skills = request.form.get('skills')
    user_stream= request.form.get('stream')
    user_persue = request.form.get('persue')

    recommend_jobs(user_skills,'JOB_recommendation/jobs.csv')
    recommend_internships(user_skills,'JOB_recommendation/internships.csv')
    recommend_exams(user_persue,'JOB_recommendation/exams.csv')
    recommend_courses(user_persue,user_stream,'JOB_recommendation/courses.csv')
    return render_template('main.html')

@app.route('/jobs')
def jobs():
    # # Execute the recommend.py file
    # subprocess.run(['python', 'recommend.py'])
    
    # Read the generated CSV file
    csv_file_path = 'JOB_recommendation/recommended_jobs.csv' 
    jobs_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            jobs_data = [row for row in reader]
    
    # Return the main page with the jobs data
    return render_template('main.html', jobs_data=jobs_data)

@app.route('/internships')
def internships():
    csv_file_path = 'JOB_recommendation/recommended_internships.csv'
    internships_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            internships_data = [row for row in reader]
    return render_template('main.html', internships_data=internships_data)

@app.route('/exams')
def exams():
    csv_file_path = 'JOB_recommendation/recommended_exams.csv'
    exams_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            exams_data = [row for row in reader]
    return render_template('main.html', exams_data=exams_data)

@app.route('/courses')
def courses():
    csv_file_path = 'JOB_recommendation/recommended_courses.csv'
    courses_data = []
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            courses_data = [row for row in reader]
    return render_template('main.html', courses_data=courses_data)

if __name__ == '__main__':
    app.run(debug=True)















