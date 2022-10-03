#Join Waktu

from telethon import TelegramClient, functions, sync, events
import time
from telethon.errors import *
from threading import *
import asyncio

def fetch_text():
    self = """ x """
    return self


def fetch_list():
    channel_list = []

    return channel_list

class ravi():
    def __init__(self,T_id,T_hash,owner):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = fetch_list()
            self.message = fetch_text()

    def connection(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash)
        self.client.start()
        print("Akun ini udah join.")

    def join_channel(self):
        for var in self.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"Akun {self.owner} udah join di {var}")
                time.sleep(300)

            except Exception as ex:
                print(ex)
                time.sleep(600)
                continue
        print("Sip udah join semua.")

    def send_message(self):
        while True:
            for var in self.channel_list:
                try:
                    entity = self.client.get_entity(var)
                    self.client.send_message(entity, self.message)
                    print(f"Pesan Terkirim")
                    time.sleep(10)
                except Exception as ex:
                    print(ex)
                    time.sleep(600)
                    continue
            time.sleep(3600)

    def account(self):
        self.connection()
        self.join_channel()
        self.send_message()

api_id = ''
api_hash = ''

id0 = ravi("","","HOS")

t1 = Thread(target=id0.account)

t1.start()

t1.join()
