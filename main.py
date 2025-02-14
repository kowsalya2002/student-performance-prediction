import os
from flask import Flask, render_template, session, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['name'].strip()
        password = request.form['pass'].strip()
        if username == 'admin' and password == 'admin':
            return "Login successful! Redirecting..."  # You can redirect to another page here
        else:
            return "Invalid username or password. Please try again."
    return render_template("index.html")

@app.route('/')
def main_page():
    return render_template("abstract.html")

@app.route('/abstract')
def abstract_page():
    return render_template("abstract.html")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        df = pd.read_csv(file_path)
        table_html = df.to_html(classes='table table-striped', index=False)
        return render_template('upload.html', table=table_html)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get subject scores from the form
        try:
            sub1 = float(request.form.get("sub1", 0))
            sub2 = float(request.form.get("sub2", 0))
            sub3 = float(request.form.get("sub3", 0))
            sub4 = float(request.form.get("sub4", 0))
            sub5 = float(request.form.get("sub5", 0))
        except ValueError:
            return "Invalid input. Please enter numeric values."

        # Calculate total and determine pass/fail
        scores = [sub1, sub2, sub3, sub4, sub5]
        total = sum(scores)
        has_failed = any(score < 40 for score in scores)

        if has_failed:
            message = f"Don't give up! Learn from mistakes and come back stronger! Total Score: {total} / 500"
            image = "static/a2.avif"  # Ensure this image exists in a "static" folder
        else:
            message = f"Congratulations! You passed! Keep up the great work! Total Score: {total} / 500"
            image = "static/a1.avif"  # Ensure this image exists in a "static" folder

        return render_template("result.html", message=message, image=image)

    return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)
