import asyncio

from BilibiliClient import BilibiliClient

client = BilibiliClient(1040)
loop = asyncio.get_event_loop()
asyncio.ensure_future(client.connect())
loop.run_forever()
loop.close()
