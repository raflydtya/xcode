import asyncio
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest

api_id = [0]
api_hash = [1]
session = [2]
locate = ["a", "b", "c", "d"]

async def join():

   async with TelegramClient(session, api_id, api_hash) as client:

     for x in locate:

            try:

                await client(JoinChannelRequest(x))

            except FloodWaitError as error:

                print(error)

                await asyncio.sleep(delay=error.seconds)

            except Exception as error:

                print(error)

asyncio.run(join())
