import os
import logging

from typing import List

from scoring import Result, Checkpoint, bonus_for_completing_any
from common import create_rocketchat_client, grader

# Create RocketChat instance
rocket = create_rocketchat_client()

@grader
def check_url(trajectory):
    return f"channel/general" in trajectory


def get_channel_room_id(channel_name):
    """Get the room_id for a specific channel by its name."""
    response = rocket.channels_info(channel=channel_name).json()
    if response.get('success'):
        return response['channel']['_id']
    return None


def get_message(channel_name, username):
    room_id = get_channel_room_id(channel_name)
    if not room_id:
        print(f"Failed to find room ID for channel #{channel_name}.")
        return False

    # Fetch message history for the channel using room_id (channel_id)
    response = rocket.channels_history(room_id=room_id).json()
    
    if response.get('success'):
        messages = response.get('messages', [])
        for msg in messages:
            if msg.get('u', {}).get('username') == username:
                return msg.get('msg')
            
    return None


@grader
def check_message_contains(message, info):
    return message is not None and info in message
    

def grade_checkpoints(trajectory=""):
    checkpoints: List[Checkpoint] = []
    result = Result(checkpoints, bonus_for_completing_any)
    checkpoints.append(Checkpoint(1, int(check_url(trajectory))))
    
    # checkpoint 2: message exists
    message = get_message("general", "theagentcompany")
    checkpoints.append(Checkpoint(1, int(message is not None)))
    
    # checkpoint 3~5: check content in the message
    checkpoints.append(Checkpoint(1, int(check_message_contains(message, "Hi"))))
    checkpoints.append(Checkpoint(1, int(check_message_contains(message, ":kissing_smiling_eyes:"))))
    checkpoints.append(Checkpoint(1, int(check_message_contains(message, "@here"))))
    
    return result



