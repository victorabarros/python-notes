import logging
import sys

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.debug('debug')
logger.info('info')
logger.error('error')
logger.exception('exception')
