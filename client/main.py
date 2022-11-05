import time
from typing import Union

from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterVoice

from client.utils import get_random_records, get_random_delay
from settings.common import API_ID, API_HASH, RECIPIENT, RANDOMIZATION_DEGREE, SENDING_TIMEOUT, SESSION_NAME
from settings.logging import logger


client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def get_voices_messages(entity):
    """Get all voices messages from chat. """
    return await client.get_messages(entity=entity, filter=InputMessagesFilterVoice)


def get_recipient_data(recipient: str) -> Union[str, int]:
    try:
        if recipient.startswith('+'):
            raise ValueError

        recipient_data = int(recipient)
    except ValueError:
        return recipient

    return recipient_data


async def main():
    me = await client.get_me()
    messages = await get_voices_messages(me)
    logger.info(msg='List of messages is loaded.')

    while True:
        message_to_send = get_random_records(messages)[0]

        recipient = get_recipient_data(RECIPIENT)
        await client.send_message(recipient, message=message_to_send)
        logger.info(f'Message sent to {recipient}.')

        delay = get_random_delay(delay=SENDING_TIMEOUT, rand_degree=RANDOMIZATION_DEGREE)
        logger.info(f'Delay {delay} seconds.')
        time.sleep(delay)


with client:
    client.loop.run_until_complete(main())
