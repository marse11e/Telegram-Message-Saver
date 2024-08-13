import os
import configparser


def install_requirements():
    print("Требования к установке ...")
    os.system('python3 -m pip install -r requirements.txt')
    os.system('pip3 install -r requirements.txt')

def setup_config():
    cpass = configparser.RawConfigParser()
    cpass.add_section('account')

    xid = input("Введите идентификатор API: ")
    cpass.set('account', 'api_id', xid)

    xhash = input("Введите хэш API: ")
    cpass.set('account', 'api_hash', xhash)

    username = input("Введите username: ")
    cpass.set('account', 'username', username)

    xphone = input("Введите номер телефона: ")
    cpass.set('account', 'phone', xphone)

    password = input("Введите пароль (Если нету нажми ENTER): ")
    cpass.set('account', 'password', password)

    channel_id = input("Введите идентификатор канала: ")
    cpass.set('account', 'channel_id', channel_id)

    with open('config.ini', 'w') as setup_file:
        cpass.write(setup_file)

    print("Настройка завершена!")


def main():
    # Установка необходимых зависимостей.
    install_requirements()
    # Настройка конфигурационного файла.
    setup_config()


if __name__ == "__main__":
    main()