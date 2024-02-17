from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, Channel, Chat
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Create the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    async with client:
        dialogs = await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,
            hash=0
        ))

        for dialog in dialogs.dialogs:
            entity = await client.get_entity(dialog.peer)
            if isinstance(entity, (Channel, Chat)):
                print(f"Group/Channel: {entity.title}, ID: {entity.id}, Access Hash: {entity.access_hash}")

with client:
    client.loop.run_until_complete(main())
