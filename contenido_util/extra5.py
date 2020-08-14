import logging as log

#filemode='w' to refresh the log file/..
a='El programa se cerro inesperadamente'
log.basicConfig(filename='logs/configuracionBasica.log',level=log.DEBUG)
log.debug('Line 11 :....')
log.info('System Bug')
log.warning(a)