from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from userbot import API_KEY, API_HASH

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")

with TelegramClient(StringSession(), 1140463, 7c8b92de6ff611a99a3acdecac2fb87a) as client:
    print(client.session.save())
