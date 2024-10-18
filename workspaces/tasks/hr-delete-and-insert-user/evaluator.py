import os
from rocketchat_API.rocketchat import RocketChat

import datetime

# Set environment variables
SERVER_HOSTNAME = os.getenv('SERVER_HOSTNAME') or 'theagentcompany.com'
ROCKETCHAT_PORT = os.getenv('ROCKETCHAT_PORT') or '3000'

# Construct RocketChat URL
ROCKETCHAT_URL = f"http://{SERVER_HOSTNAME}:{ROCKETCHAT_PORT}"

# Set admin credentials
ADMIN_USERNAME = 'jobbench'
ADMIN_PASSWORD = 'jobbench'

# Create RocketChat instance
rocket = RocketChat(ADMIN_USERNAME, ADMIN_PASSWORD, server_url=ROCKETCHAT_URL)

def check_user_added(channel_name, username):
    members = rocket.channels_members(channel=channel_name).json()
    users_list = members.get("members")
    return any(user['username'] == username for user in users_list)

def check_user_removed(username):
    response_user = rocket.users_info(username=username).json()
    is_exist = response_user['success']
    return not is_exist

def check_user_exist(username):
    response_user = rocket.users_info(username=username).json()
    is_exist = response_user['success']
    return is_exist

def checkpoint1(username='li_ming'):
    return check_user_removed(username=username)

def checkpoint2(username='dandan_liu'):
    return check_user_exist(username=username)

def checkpoint3(channel_name='product', username='dandan_liu'):
    return check_user_added(channel_name=channel_name,username=username)

def calculate_total_score():
    # Define the scores corresponding to when each function is True
    scores = {
        checkpoint1: 1,
        checkpoint2: 1,
        checkpoint3: 1
    }

    total_score = 0

    for func, score in scores.items():
        if func():
            total_score += score

    return total_score

# compute the total point
total = calculate_total_score()
print(f"\ntotal point is: {total}")

