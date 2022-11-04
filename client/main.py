from telethon import TelegramClient

from settings.common import API_ID, API_HASH, RECIPIENT_USERNAME, SESSION_NAME


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def main():
    await client.send_message(RECIPIENT_USERNAME, message='Testing!')


with client:
    client.loop.run_until_complete(main())
