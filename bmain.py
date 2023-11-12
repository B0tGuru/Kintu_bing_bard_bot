import logging
import sys
import time
import bot,main
import daemonocle,uvicorn,asyncio

async def startServer():
    await uvicorn.run(main.app, host="0.0.0.0", port=8080)
def main():
    asyncio.create_task(bot.main)
    #print("server started")
    #await main.app
    #startServer()
    #bot.main()
    #logging.basicConfig(
    #    filename='bardbot.log',
    #    level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
    #)
    #logging.info('Daemon is starting')
    #while True:
    #    logging.debug('Still running')
    #    time.sleep(10)
    #await bot.main()
#asyncio.run(main())
#if __name__ == '__main__':
#    daemon = daemonocle.Daemon(
#        worker=main, pid_file='bardcle.pid'
       
#    )
#    daemon.do_action(sys.argv[1])
#main()
