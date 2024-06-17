import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty):
    points_of_winning = difficulty * 3 + 5
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = int(f.read())
    except (FileNotFoundError, ValueError):
        score = 0

    with open(SCORES_FILE_NAME, 'w') as f:
        f.write(str(score + points_of_winning))
