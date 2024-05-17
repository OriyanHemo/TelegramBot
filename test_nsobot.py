import pytest
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.custom.message import Message
from dotenv import load_dotenv
from typing import Final
import os

load_dotenv()  # take environment variables from .env.

BOT_USERNAME: Final = os.getenv("BOT_USERNAME")
TELEGRAM_APP_ID: Final = os.getenv("TELEGRAM_APP_ID")
TELEGRAM_APP_HASH: Final = os.getenv("TELEGRAM_APP_HASH")
TELETHON_SESSION: Final = os.getenv("TELETHON_SESSION")

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture(scope="session")
async def conv():
    client = TelegramClient(
        StringSession(TELETHON_SESSION), TELEGRAM_APP_ID, TELEGRAM_APP_HASH,
        sequential_updates=True
    )
    await client.connect()
    async with client.conversation(BOT_USERNAME) as conv:
        yield conv

@pytest.mark.anyio
async def test_start(conv):
    await conv.send_message("/start")
    resp: Message = await conv.get_response()
    assert "[*] Welcome 0x1on! upload your JPG/JPEG images and get their hashes." in resp.raw_text


@pytest.mark.anyio
async def test_msg_handler(conv):

    await conv.send_file( "./images/default.jpg")
    resp: Message = await conv.get_response()
    assert "[*] The md5 hash of the image is: 1cec024041c1a7d9842f7925a145d20c" in resp.raw_text

    await conv.send_file( "./images/default.gif")
    resp: Message = await conv.get_response()
    assert "[x] The received message is not an image." in resp.raw_text

#python3 -m pytest test_nsobot.py