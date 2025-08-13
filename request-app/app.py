
from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
import os
import json
from datetime import datetime
from config import Config
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from user import User


app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
SUBMISSIONS_DIR = Config.SUBMISSIONS_DIR
os.makedirs(SUBMISSIONS_DIR, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app_name = request.form.get('app_name')
        environment = request.form.getlist('environment')
        platform = request.form.get('platform')
        project_code = request.form.get('project_code')

        if not app_name or not environment or not platform or not project_code:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        submission_id = str(uuid.uuid4())
        data = {
            'id': submission_id,
            'app_name': app_name,
            'environment': environment,  # This will be a list
            'platform': platform,
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
