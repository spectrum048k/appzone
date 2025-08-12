from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

SUBMISSIONS_DIR = os.path.join(os.path.dirname(__file__), 'submissions')
os.makedirs(SUBMISSIONS_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app_name = request.form.get('app_name')
        environment = request.form.get('environment')
        project_code = request.form.get('project_code')

        if not app_name or not environment or not project_code:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        submission_id = str(uuid.uuid4())
        data = {
            'id': submission_id,
            'app_name': app_name,
            'environment': environment,
            'project_code': project_code,
            'timestamp': datetime.utcnow().isoformat()
        }
        filename = f"{submission_id}.json"
        filepath = os.path.join(SUBMISSIONS_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        flash(f'Submission saved successfully! Your request ID is: {submission_id}', 'success')
        return redirect(url_for('index'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
