import os
# Import from local codebase rather than package. Because there is a bug in RocketChatBot
from RocketChatBot import RocketChatBot

botname = os.getenv('BOTNAME') or "rocket.cat"
botpassword = os.getenv('BOTPASSWORD') or "jobbench"
server_url = os.getenv('BOT_URL') or 'http://localhost:3000'
# server_url = 'ogma.lti.cs.cmu.edu:3000'

bot = RocketChatBot(botname, botpassword, server_url)
bot.add_auto_answer(['good news', 'i have good news', ], ['hell yeah!', 'tell me, tell me!', 'you are already good news ;)', ])
bot.add_direct_answer(['who are you?', 'what is your name?', ], ['I am botname', ])

bot.run()
