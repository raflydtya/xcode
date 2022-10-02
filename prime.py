import time
import asyncio
import sys
import random
from telethon import TelegramClient, events, utils, Button

api_id = [0]
api_hash = [1]
sesi = [{2}, {3}]
client = TelegramClient(sesi, api_id, api_hash)

# Dest STRING
[4] = [5]
[6] = [7]
[8] = [9]
[10] = [11]

# Cmd STRING
[12] = [13]
[14] = [15]

makro = True

#Definisi
async def jeda(w):
   await asyncio.sleep(w)

async def [16](client,w):
   while True:
        await client.send_message([17], [18])
        await jeda(w)
        
async def [19](client,w):
   while True:
       await client.send_message([20], [21])
       await jeda(w)
       
@client.on(events.NewMessage(from_users=[22]))
async def handler(event):
        x = event.raw_text
        global makro
        
        if [23] in x:
            time.sleep(2)
            await event.respond([24])
            return  

        elif [25] in pesan:
            time.sleep(2)
            await event.respond([26])
            print(time.asctime(), '[27]')
            return

with client:
    client.loop.create_task([28](client, {time}))
    client.loop.create_task([29](client, {time}))
    client.run_until_disconnected()
