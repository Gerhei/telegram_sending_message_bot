from settings import config


API_ID = config('API_ID')
API_HASH = config('API_HASH')
SESSION_NAME = config('SESSION_NAME', default='session')

RECIPIENT_USERNAME = config('RECIPIENT_USERNAME', default='')
RECIPIENT_PHONE = config('RECIPIENT_PHONE', default='')
RECIPIENT_USER_ID = config('RECIPIENT_USER_ID', default='')
