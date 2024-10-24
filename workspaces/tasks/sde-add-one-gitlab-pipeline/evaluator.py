import sys
import requests
import logging
from common import *

# Configuration for gitlab
project_path = "root/openhands"


def get_gitlab_pipeline():
    try:
        response = make_gitlab_request(project_path, "pipelines")
        return response.json()
    except Exception as e:
        logging.error(f"Error occurred while checking the repository: {e}")
        return {}


def checkpoint1(url='http://the-agent-company.com:8929/root/openhands/-/ci/editor?branch_name=main'):
    if len(sys.argv) < 2:
        trajectory = ""
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                trajectory = file.read()
        except Exception as e:
            print(f"Error reading trajectory file: {e}")
            exit(1)
    return url in trajectory


def checkpoint2():
    msgs = get_gitlab_pipeline()
    return bool(msgs)


def calculate_total_score():
    # Define the scores corresponding to when each function is True
    scores = {
        checkpoint1: 1,
        checkpoint2: 2
    }

    total_score = 0

    for func, score in scores.items():
        if func():
            total_score += score

    return total_score

# compute the total point
total = calculate_total_score()
print(f"\ntotal point is: {total}")
