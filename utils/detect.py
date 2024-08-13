from geopy.geocoders import Nominatim
from pyrogram.types import Message, Chat, User


def get_location_address(latitude: str, longitude: str) -> str:
    geolocator = Nominatim(user_agent="my_geolocator")
    location = geolocator.reverse((latitude, longitude), language="ru", namedetails=True)
    if location is None:
        return "Адрес не найден"
    else:
        return location.address


def get_fullname(user: User) -> str:
    if user.first_name and user.last_name:
        return f"{user.first_name} {user.last_name} (@{user.username})"
    
    elif user.first_name and user.username:
        return f"{user.first_name} (@{user.username})"

    elif user.username:
        return f"@{user.username}"
    
    else:
        return f"Анонимный ({user.id})"


def user_info(user: User) -> str:
    username = ""

    if user.username:
        username = f"(@{user.username})"

    return (
        f"Написал(а):\n"
        f"#ID{user.id} | {user.first_name if hasattr(user, 'first_name') else ''} {user.last_name if hasattr(user, 'last_name') else ''} {username}\n"
        f"\n"
    )


def chat_info(chat: Chat) -> str:
    username = ""

    if chat.username:
        username = f"(@{chat.username})"

    return (
        f"Чат:\n"
        f"#ID{chat.id} | {chat.first_name if hasattr(chat, 'first_name') else ''} {chat.last_name if hasattr(chat, 'last_name') else ''} {username}\n"
        "\n"
    )


def message_text(message: Message):
    return user_info(message.from_user) + chat_info(message.chat) + f"Сообщения: {message.text}\n\n" + f"#MID{message.id}"


def message_photo(message: Message):
    print(message)
    caption = (
        f"Размер: {message.photo.file_size} байт\nРазмеры: {message.photo.width}x{message.photo.height}\n\n"
        f"#MID{message.id}"
    )
    return user_info(message.from_user) + chat_info(message.chat) + caption


def message_document(message: Message):
    caption = (
        f"Имя файла: {message.document.file_name}\n"
        f"MIME-тип: {message.document.mime_type}\n"
        f"Размер файла: {message.document.file_size} байт\n"
    )
    if message.document.thumbs: caption += f"Миниатюра: {message.document.thumbs[-1].width} x {message.document.thumbs[-1].height}\n\n"
    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_video(message: Message):
    caption = (
        f"Имя файла: {message.video.file_name}\n"
        f"MIME-тип: {message.video.mime_type}\n"
        f"Размер файла: {message.video.file_size} байт\n"
        f"Размеры: {message.video.width}x{message.video.height}\n"
        f"Продолжительность: {message.video.duration}\n\n"
    )
    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_sticker(message: Message):
    caption = (
        f"Размер: {message.sticker.file_size} байт\n"
        f"Размеры: {message.sticker.width}x{message.sticker.height}\n"
        f"Эмодзи: {message.sticker.emoji}\n"
        f"Название набора: {message.sticker.set_name}\n"
        f"Эмодзи анимированного стикера: {message.sticker.is_animated}\n"
        f"Эмодзи видео стикера: {message.sticker.is_video}\n"
        f"Тип стикера: {message.sticker.type}\n"
        f"Миниатюра: {message.sticker.thumbs[-1].width} x {message.sticker.thumbs[-1].height}\n\n"
    )
    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_videonote(message: Message):
    caption = (
        f"Продолжительность: {message.video_note.duration} секунд\n"
        f"Размер файла: {message.video_note.file_size} байт\n"
        f"Размер миниатюры: {message.video_note.thumbs[-1].file_size} байт\n\n"
    )

    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_voice(message: Message):
    caption = (
        f"MIME-тип: {message.voice.mime_type}\n"
        f"Размер файла: {message.voice.file_size}\n"
        f"Продолжительность: {message.voice.duration}\n\n"
    )
    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_location(message: Message):
    address = get_location_address(message.location.latitude, message.location.longitude)

    caption = (
        f"Информация о местоположении:\n"
        f"<code>{address}</code>\n"
        f"\n"
        f"Latitude: {message.location.latitude}\n"
        f"Longitude: {message.location.longitude}\n\n"
    )

    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_venue(message: Message):
    caption = (
        f"Информация о местоположении:\n"
        f"Название: <code>{message.venue.title}</code>\n"
        f"Адрес: <code>{message.venue.address}</code>\n"
        f"\n"
        f"Latitude: {message.venue.location.latitude}\n"
        f"Longitude: {message.venue.location.longitude}\n\n"
    )

    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_contact(message: Message):
    caption = (
        f"ID пользователя: {message.contact.user_id}\n"
        f"Имя: {message.contact.first_name}\n"
        f"Номер телефона: {message.contact.phone_number}\n"
        f"Карточка: <code>{message.contact.vcard}</code>\n"
    )

    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_audio(message: Message):
    caption = (
        f"Исполнитель: {message.audio.performer}\n"
        f"Название: {message.audio.title}\n"
        f"Имя файла: {message.audio.file_name}\n"
        f"MIME-тип: {message.audio.mime_type}\n"
        f"Продолжительность: {message.audio.duration} секунд\n"
        f"Размер файла: {message.audio.file_size} байт\n"
    )

    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_animation(message: Message):
    caption = (
        f"Имя файла: {message.animation.file_name}\n"
        f"MIME-тип: {message.animation.mime_type}\n"
        f"Размер файла: {message.animation.file_size} байт\n"
        f"Размеры: {message.animation.width}x{message.animation.height}\n"
        f"Продолжительность: {message.animation.duration}\n"
    )

    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def detection_of_an_unknown_message_type(message: Message):
    caption = f"Неизвестный тип сообщения:\n"
    caption += f"<code>{message}</code>\n\n"
    return user_info(message.from_user) + chat_info(message.chat) + caption + f"#MID{message.id}"


def message_deleted(messages: Message):
    caption = "Удаленные сообщения:\n"

    for message in messages:
        caption += f"#MID{message.id}\n"

    return caption


def message_update(message: Message):
    caption = (
        f"Сообщения: #MID{message.id}\n"
        f"Изменено на: {message.text}"
    )
    return user_info(message.from_user) + chat_info(message.chat) + caption


def user_status_update(user: User):
    caption = (
        f"Статус пользователя:\n"
        f"Имя: {get_fullname(user)}\n"
    )
    
    if user.next_offline_date:
        return caption + \
            f"Статус: {user.status.value} 🟢\n\n" + \
            f"#ID{user.id}\n\n"
        
    return caption + \
        f"Статус: {user.status.value} 🔴\n" + \
        f"Дата последнего онлайна: {user.last_online_date}\n\n" + \
        f"#ID{user.id}\n\n"
