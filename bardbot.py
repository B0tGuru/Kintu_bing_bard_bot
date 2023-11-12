from os import environ
from Bard import Chatbot


token = environ.get("BARD_TOKEN")

#environ.get("BARD_TOKEN")
def initBard(bard_token):
    token = bard_token
async def bardChat(bard_msg):
    chatbot = Chatbot(token)

    bot_reply = chatbot.ask(bard_msg)
    return bot_reply['content']