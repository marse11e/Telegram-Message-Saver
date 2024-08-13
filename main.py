import os
import sys
import json
import logging
from random import choice

from pyrogram import Client, filters
from pyrogram.types import Message, Chat, User

from core.settings import (
    API_ID, API_HASH, USERNAME, PHONE, PASSWORD, CANNEL_ID, CANNEL_2_ID
)
from utils.detect import (
    message_text, message_photo, message_document, message_video,
    message_sticker, message_videonote, message_voice, message_location,
    message_venue, message_contact, message_audio, message_animation,
    detection_of_an_unknown_message_type, message_deleted, message_update,
    user_status_update
)


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("app.log"),
    ]
)

logger = logging.getLogger(__name__)

APP = Client(name=USERNAME, api_id=API_ID, api_hash=API_HASH,
             phone_number=PHONE, password=PASSWORD)


@APP.on_message(filters=filters.private)
async def my_handler_message(client: Client, message: Message):
    if message.text:
        await client.send_message(CANNEL_ID, text=message_text(message))

    elif message.photo:
        await client.send_photo(CANNEL_ID, photo=message.photo.file_id, caption=message_photo(message))

    elif message.document:
        await client.send_document(CANNEL_ID, document=message.document.file_id, caption=message_document(message))

    elif message.video:
        await client.send_video(CANNEL_ID, video=message.video.file_id, caption=message_video(message))

    elif message.sticker:
        await client.send_sticker(CANNEL_ID, sticker=message.sticker.file_id)
        await client.send_message(CANNEL_ID, text=message_sticker(message))

    elif message.video_note:
        await client.send_video_note(CANNEL_ID, video_note=message.video_note.file_id)
        await client.send_message(CANNEL_ID, text=message_videonote(message))

    elif message.voice:
        await client.send_voice(CANNEL_ID, voice=message.voice.file_id, caption=message_voice(message))

    elif message.location:
        await client.send_location(CANNEL_ID, latitude=message.location.latitude, longitude=message.location.longitude)
        await client.send_message(CANNEL_ID, text=message_location(message))

    elif message.venue:
        await client.send_venue(CANNEL_ID, latitude=message.venue.location.latitude,
                                longitude=message.venue.location.longitude,
                                title=message.venue.title, address=message.venue.address)
        await client.send_message(CANNEL_ID, text=message_venue(message))

    elif message.contact:
        await client.send_contact(CANNEL_ID, phone_number=message.contact.phone_number, first_name=message.contact.first_name)
        await client.send_message(CANNEL_ID, text=message_contact(message))

    elif message.audio:
        await client.send_audio(CANNEL_ID, audio=message.audio.file_id, caption=message_audio(message))

    elif message.animation:
        await client.send_animation(CANNEL_ID, animation=message.animation.file_id, caption=message_animation(message))

    else:
        await client.send_message(CANNEL_ID, text=detection_of_an_unknown_message_type(message))


@APP.on_deleted_messages()
async def my_handler_deleted_messages(client: Client, message: Message):
    await client.send_message(CANNEL_ID, text=message_deleted(message))


@APP.on_edited_message(filters=filters.private)
async def my_handler_edited_message(client: Client, message: Message):
    await client.send_message(CANNEL_ID, text=message_update(message))


@APP.on_user_status()
async def my_handler_user_status(client: Client, message: Message):
    try:
        user_info_from_id = await client.get_users(message.id)

    except Exception as ex:
        logger.debug(f"{ex} Неизвестный статус пользователя ({message.id})")
        
    else:
        await client.send_message(CANNEL_2_ID, text=user_status_update(user_info_from_id))


if __name__ == '__main__':
    try:
        os.system('clear')
        logger.info("Starting the application...")
        APP.run()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
