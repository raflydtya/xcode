#Join Bareng

from telethon import TelegramClient, functions, sync, events
import time
from telethon.errors import *
from threading import *
import asyncio

def fetch_text():
    self = """ """ # Pesan
    return self

def group0():
    channel_list = [] # Username Grup Akun Ke 0

    return channel_list

def group1():
    channel_list = [] # Username Grup Akun Ke 1

    return channel_list

def group2():
    channel_list = [] # Username Grup Akun ke 2

    return channel_list

def group3():
    channel_list = [] # Username Grup Akun ke 3

    return channel_list

def group4():
    channel_list = [] # Username Grup Akun ke 4

    return channel_list

group0 = group0()
group1 = group1()
group2 = group2()
group3 = group3()
group4 = group4()

class ravi():
    def __init__(self,T_id,T_hash,owner,group):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = group
            self.message = fetch_text()

    def connection(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash)
        self.client.start()
        print("Akunnya udah join.")

    def join_channel(self):
        for var in self.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"Akun {self.owner} join {var}")
                time.sleep(300)

            except Exception as ex:
                print(ex)
                time.sleep(600)
                continue
        print("Sip, Semua akun udah join semua")

    def send_message(self):
        while True:
            i=0
            for var in self.channel_list:
                try:
                    if i < 20:
                        entity = self.client.get_entity(var)
                        self.client.send_message(entity, self.message)
                        print(f"Pesan Terkirim")
                        print("________________________________________")
                        i+=1
                        time.sleep(5)
                    else:
                        i=0
                        time.sleep(300)
                except Exception as ex:
                    print(ex)
                    time.sleep(10)
                    continue

    def account(self):
        self.connection()
        self.join_channel()
        self.send_message()

api_id = ''
api_hash = ''
#sesi_file = ''

id0 = ravi(api_id,api_hash,"0",group0) #Akun 0 
id1 = ravi(api_id,api_hash,"1",group1) #Akun 1
id2 = ravi(api_id,api_hash,"2",group2) #Akun 2
id3 = ravi(api_id,api_hash,"3",group3) #Akun 3
id4 = ravi(api_id,api_hash,"4",group4) #Akun 4

t1 = Thread(target=id0.account)
t2 = Thread(target=id1.account)
t3 = Thread(target=id2.account)
t4 = Thread(target=id3.account)
t5 = Thread(target=id4.account)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
