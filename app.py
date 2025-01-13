from flask import Flask, request, render_template, redirect, url_for
from supabase import create_client, Client
import os



SUPABASE_URL = os.environ['url']
SUPABASE_KEY =os.environ['key']
# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



# Initialize Flask app
app = Flask(__name__)

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to render the form
@app.route('/contact.html')
def contact_form():
    return render_template('contact.html')

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
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
