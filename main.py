import nest_asyncio
from telegram import Update
nest_asyncio.apply()
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
#from telegram.utils.asyncio import run_coroutine_threadsafe
import asyncio,threading
import subprocess,aibot,os
import logging
import logging.config

logger = logging.getLogger(__name__)
app = FastAPI()
athd = None

#bard_token = os.environ.get("BARD_TOKEN")
#tele_token =  os.environ.get("TELE_TOKEN")
web_url =  os.environ.get("WEB_URL")

#aibot.
#3991
#loop = asyncio.get_event_loop()
class TelegramUpdate(BaseModel):
    update_id: int
    message: dict

@app.get("/")
async def root():
    #portin = os.environ.get("UVICORN_PORT")
    #print(f"started: {portin}")
    logged = aibot.logs
    return f"HELLOWORLD , WELCOME TO MYSPACES, Great love from space! 🚀: man\n {logged}"

def start_bot():
    print("bot started")
    loop = asyncio.new_event_loop()
    loop.create_task(bot.main())
    #bot.main()
logger.error(" app okayed")
@app.on_event("startup")
async def startup_event():
    #portin = os.environ.get("UVICORN_PORT")
    #print(f"started: {portin}")
    #aibot.logs.append(f"web event started")
    logger.error(" xapp started")
    logging.error("xapp startup")
    await aibot.main(web_url)
    logging.error("app init finished")
    logger.error(" xapp init fined")
   #threading.Thread(target=start_bot).start()
    #loop = asyncio.get_event_loop()
    #(bot.main()))
    #app.bg_task = asyncio.create_task(start_bot())
print("event loop ok")
#asyncio.set_event_loop(loop)
#loop.run_forever()
@app.get("/mefile")#, response_class=HTMLResponse)
async def get_index():
    return "okay index"
    # Load the index.html file
    #with open("hi.mp3") as f:
    #    index_html = f.read()
    #if index_html == None:
    #    return "file error"
    #else:
    #    return index_html
@app.post("/tbard/webhook")
async def telegram_webhook(request: Request):
    aibot.logs.append(f"gotten data")
    logging.error("data here")
    logger.info("obtained some data")
    json_req = await request.json()
    print("request clear")
    #aibot.logs.append(f"gotten data {json_req}")
    update_in = Update.de_json(json_req, aibot.tapp.bot)
    #update_in = await abot.get_updates(limit=100)
    updates_len = 0#len(update_in)
    #print(update)
    #aibot.logs.append(update_in)
    #aibot.logs.append(":update_ends_here:")
    #aibot.logs.append(f"updates size: {updates_len}")
    #await 
    #await aibot.tapp.process_update(update_in)
    usr_req = threading.Thread(target= startProcess,args=(update_in,))#aibot.tapp.process_update, args=(update_in,))
    usr_req.start()
    #asyncio.create_task((aibot.tapp.process_update(update_in)))
    #handle_update(update)
    return {"status": "ok"}

def startProcess(request_in):
    active_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(active_loop)
    active_loop.run_until_complete(aibot.tapp.process_update(request_in))
    active_loop.close()
    print("starting process")
#asyncio.set_event_loop(loop)

#import uvicorn
#uvicorn.run(app, host="0.0.0.0", port=8080)
#asyncio.create_task(start_bot())