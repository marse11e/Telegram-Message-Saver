import configparser
import os


CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')


API_ID = CONFIG.getint('account', 'api_id')
API_HASH = CONFIG.get('account', 'api_hash')
USERNAME = CONFIG.get('account', 'username')
PHONE = CONFIG.get('account', 'phone')
PASSWORD = CONFIG.get('account', 'password')
CANNEL_ID = CONFIG.get('account', 'channel_id')
# USER_ID = CONFIG.getint('account', 'user_id')

# Test
# USER_ID_1 = CONFIG.getint('Customer_ids', 'user_id_1')
# USER_ID_2 = CONFIG.getint('Customer_ids', 'user_id_2')
# USER_ID_3 = CONFIG.getint('Customer_ids', 'user_id_3')
# USER_ID_4 = CONFIG.getint('Customer_ids', 'user_id_4')
# USER_ID_5 = CONFIG.getint('Customer_ids', 'user_id_5')
# USER_ID_6 = CONFIG.getint('Customer_ids', 'user_id_6')