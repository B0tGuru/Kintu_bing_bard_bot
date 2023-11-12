from os import environ
from Bard import Chatbot

#token = "YgiUwjZzvcgJZh1gYq6qMlsc9YGs1kYVVAXor091QZsw3Z42nSrVJcqLLCJVsNIiAFhCiQ."
token = environ.get("BARD_TOKEN")
#"ZwiUwjHtquauyGO5GhAYqv0F3-KmdNafVgHwWEUeTncC-NRx8tlZWbXK16WCuZWoEFhgJA."
#token = "XQiUwvC1lIV8hVqcyfL1g_bJO6eX9F_dxhYCxN7lgz0cNOVaFeKzfxloKn1dINHVKi_Vog."
#environ.get("BARD_TOKEN")
def initBard(bard_token):
    token = bard_token
async def bardChat(bard_msg):
    chatbot = Chatbot(token)

    bot_reply = chatbot.ask(bard_msg)
    return bot_reply['content']