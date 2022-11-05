from settings import config


API_ID = config('API_ID')
API_HASH = config('API_HASH')
SESSION_NAME = config('SESSION_NAME', default='session')

RECIPIENT = config('RECIPIENT')

SENDING_TIMEOUT = config('SENDING_TIMEOUT', cast=int)
RANDOMIZATION_DEGREE = config('RANDOMIZATION_DEGREE', cast=float)
