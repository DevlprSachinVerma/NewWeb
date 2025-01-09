from flask import Flask, request, render_template, redirect, url_for
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = "https://zhcipbwwskmneifittsc.supabase.co"  # Replace with your Supabase URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpoY2lwYnd3c2ttbmVpZml0dHNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzYxNTYyOTcsImV4cCI6MjA1MTczMjI5N30.CChd_lF5slA6Zfmo1I43Fcq0pew7pGi0tWOJROOIzi0"                    # Replace with your Supabase API Key
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize Flask app
app = Flask(__name__)

# Route to render the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route to render the form
@app.route('/contact')
def contact_form():
    return render_template('contact_form.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    phone = int(request.form['phone'])
    exam = request.form['exam']
    question = request.form.get('question', '')

    print(type(name))
    print(type(phone))
    print(type(exam))
    print(type(question))
    # Insert data into Supabase
    response = supabase.table('contact').insert({
        "name": name,
        "phone": phone,
        "exam": exam,
        "question": question
    }).execute()

    # Handle response
    if not response.data:  # If `data` is empty, there's an issue
        print("Error occurred:", response)
        return "Error occurred while inserting data.", 500
    return render_template('submitted.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
