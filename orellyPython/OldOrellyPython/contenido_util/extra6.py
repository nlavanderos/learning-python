import logging
import logging.config

logging.config.fileConfig('/home/setxh/Desktop/libritoCode/confs/ejercicioRegistro.conf')


# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

