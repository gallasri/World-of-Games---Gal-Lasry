from flask import Flask, render_template
from Score import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = int(f.read())
    except (FileNotFoundError, ValueError):
        return render_template('error.html', error=BAD_RETURN_CODE)

    return render_template('score.html', score=score)
