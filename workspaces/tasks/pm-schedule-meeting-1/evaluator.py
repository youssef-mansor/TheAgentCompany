import os
import logging

from typing import List

from scoring import Result, Checkpoint
from common import evaluate_with_llm
from common import create_rocketchat_client

# Create RocketChat instance
rocket = create_rocketchat_client()


def get_history(username):
    id = ""
    tmp = rocket.users_list().json()['users']
    for item in rocket.users_list().json()['users']:
        if item['username'] == username:
            id = item["_id"]
            break
    msgs = rocket.im_history(room_id=id).json()['messages']
    for msg in msgs[::-1]:
        print(f"{username}'s chat: {msg['msg']}")

    if len(msgs)>0:
        return True
    else:
        return False

def check_final_result(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"The file {file_path} does not exist.")
        return False

    # Read the content of the file and call litellm
    content = ''
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    if len(content) == 0:
        logging.warning("there is no content in the txt")
        return False

    predicate = 'a meeting is scheduled'
    return evaluate_with_llm(content, predicate)


def checkpoint1(username='emily_zhou'):
    return get_history(username=username)

def checkpoint2(username='liu_qiang'):
    return get_history(username=username)

def checkpoint3(file_path = '/workspace/conclusion.txt'):
    return check_final_result(file_path=file_path)


def grade_checkpoints(trajectory=""):
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints)

    # Define the scores corresponding to when each function is True
    scores = {
        checkpoint1: 1,
        checkpoint2: 2,
        checkpoint3: 3
    }

    for func, total_score in scores.items():
        checkpoints.append(Checkpoint(total_score, total_score * int(func())))

    return result



