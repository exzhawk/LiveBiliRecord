import asyncio
import logging

from BilibiliClient import BilibiliClient

while True:
    try:
        client = BilibiliClient(1040)
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(client.connect())
        loop.run_forever()
    except ConnectionResetError as e:
        logging.warning(e)
    except KeyboardInterrupt as e:
        logging.warning(e)
        break
    finally:
        loop.close()
