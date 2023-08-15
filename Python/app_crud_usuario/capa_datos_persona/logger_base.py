import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[log.FileHandler('capa_datos.log'), log.StreamHandler()],
                encoding='utf-8')

if __name__ == '__main__':
    log.debug('Mensaje nivel DEBUG')
    log.info('Mensaje nivel INFO')
    log.warning('Mensaje nivel WARING')
    log.error('Mensaje nivel ERROR')
    log.critical('Mensaje nivel CRITICAL')