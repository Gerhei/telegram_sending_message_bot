import logging


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO, handlers=[logging.FileHandler('client.log')])

logger = logging.getLogger('telegram-client')
logger.addHandler(logging.StreamHandler())
