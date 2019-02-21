import logging

logging.basicConfig(filename='../log/logger.log',format='levelname:%(levelname)s filename: %(filename)s '
                                                 'functionName:%(funcName)s lingNum:%(lineno)d time:%(asctime)s proccessID:%(process)d ',
                    datefmt='[%d/%b/%Y %H:%M:%S]',level=logging.INFO)

# logging.debug('debug message')
# logging.info('INFO message:')
# logging.warn('warn message')
# logging.error('error message')
# logging.critical('critical message')