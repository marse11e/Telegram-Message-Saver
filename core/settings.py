import configparser
import os


CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')


API_ID = CONFIG.getint('account', 'api_id')
API_HASH = CONFIG.get('account', 'api_hash')
USERNAME = CONFIG.get('account', 'username')
PHONE = CONFIG.get('account', 'phone')
PASSWORD = CONFIG.get('account', 'password')
# USER_ID = CONFIG.getint('account', 'user_id')


# CANNEL_ID For sending private messages
CANNEL_ID = CONFIG.get('account', 'channel_id')

# CANNEL_2_ID For sending user status
CANNEL_2_ID = CONFIG.get('account', 'channel_2_id')
