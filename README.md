# Сохранение Сообщений в Телеграм

Этот проект представляет собой Telegram-бота, который автоматически сохраняет все сообщения, отправленные вам пользователями в Телеграме, и сохраняет их в указанном канале. Бот поддерживает различные типы сообщений, включая текст, фотографии, документы, видео и многое другое.

## Возможности

- Сохраняет все входящие личные сообщения в указанный канал.
- Поддерживает широкий спектр типов сообщений (текст, фотографии, документы, видео, стикеры и т.д.).
- Автоматически обрабатывает удаленные и отредактированные сообщения.
- Использует библиотеку Pyrogram для интеграции с Telegram API.
- Использует Geopy для определения адресов.

## Необходимые данные

Для запуска этого проекта вам понадобятся:

- **API ID** и **API Hash**: Получите их на официальном сайте Telegram [my.telegram.org](https://my.telegram.org).
- **Username**: Ваше имя пользователя в Телеграм.
- **Номер телефона**: Номер телефона вашего аккаунта в Телеграм.
- **Пароль**: Пароль вашего аккаунта в Телеграм.
- **ID канала**: ID канала, в который будут сохраняться все сообщения.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/marse11e/Telegram-Message-Saver
   cd Telegram-Message-Saver
   ```

2. Установите необходимые зависимости:

   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   pip3 install -r requirements.txt
   ```

3. Настройте проект:

   ```bash
   python3 setup.py
   ```

4. Введите данные вашего аккаунта Telegram в файле `core/settings.py`:

   ```python
   api_id = 'your_api_id'
   api_hash = 'your_api_hash'
   username = 'your_username'
   phone = 'your_phone_number'
   password = 'your_password'
   channel_id = 'your_channel_id'
   ```

## Использование

Чтобы запустить бота, просто выполните главный скрипт:

```bash
python3 main.py
```

Бот начнет слушать входящие сообщения и сохранять их в указанный вами канал.

## Используемые библиотеки

- **Pyrogram**: Современная и простая в использовании библиотека клиента Telegram на Python. [Документация Pyrogram](https://docs.pyrogram.org/intro/quickstart)
- **Geopy**: Клиент на Python для популярных веб-сервисов геокодирования.

## Лицензия

Этот проект распространяется по [лицензии](LICENSE) MIT.
