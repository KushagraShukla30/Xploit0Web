from flask import Flask, render_template, request
from utils import clone_repo
from scanner import scan_python, scan_node
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form['repo_url']
        local_path = clone_repo(url)

        result = None
        if os.path.exists(f"{local_path}/requirements.txt"):
            result = scan_python(f"{local_path}/requirements.txt")
        elif os.path.exists(f"{local_path}/package.json"):
            result = scan_node(local_path)

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

