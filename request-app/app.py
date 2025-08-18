from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
import os
import json
from datetime import datetime
from config import Config


app = Flask(__name__)
app.secret_key = Config.SECRET_KEY
CONFIG_DIR = Config.CONFIG_DIR
os.makedirs(CONFIG_DIR, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        app_name = request.form.get('app_name')
        environment = request.form.get('environment')
        network = request.form.get('network')
        region = request.form.get('region')
        platform = request.form.get('platform')
        project_code = request.form.get('project_code')

        if not app_name or not environment or not network or not region or not platform or not project_code:
            flash('All fields are required!', 'error')
            return redirect(url_for('index'))

        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        safe_platform = platform.replace(' ', '')
        safe_app_name = app_name.replace(' ', '')
        safe_environment = environment.replace(' ', '')
        filename = f"{safe_platform}_{safe_app_name}_{safe_environment}_{timestamp}.json"
        data = {
            'app_name': app_name,
            'environment': environment,
            'network': network,
            'region': region,
            'platform': platform,
            'project_code': project_code,
            'timestamp': timestamp
        }
        filepath = os.path.join(CONFIG_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        flash(f'Submission saved successfully! Your request file is: {filename}', 'success')
        return redirect(url_for('index'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
