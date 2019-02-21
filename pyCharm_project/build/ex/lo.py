import logging

logging.basicConfig(level=logging.INFO,filename='log.log',
                    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

# logging.info("fedfd")
logging.debug('debug info')
logging.info('hello 51zxw ！')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')

# import logging
# # import logging.config
#
# logging.basicConfig(level=logging.INFO,filename='log.log',
#                     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
#
# # logging.config.fileConfig('log.conf', defaults=None,disable_existing_loggers=True)
#
# logging.debug('debug info')
# logging.info('hello SB')
# logging.warning('warning info')
# logging.error('error info')
# logging.critical('critical info')
#
#
# # CON_LOG = 'log.conf'
# # logging.config.fileConfig(CON_LOG)
# # logging = logging.getLogger()
#
# try:
#     print(feaf)
# except Exception as e:
#     logging.warning(e)