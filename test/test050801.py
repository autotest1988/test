import time


class Loginfo():
    def __init__(self, url = '', mode = 'w'):
        filename = url + time.strftime('%%Y-%m-%d', time.gmtime()) + '.txt'
        self.log = open(filename, mode)

    def log_write(self, msg):
        self.log.write(msg)

    def log_close(self):
        self.log.close()


if __name__ == '__main__':
    log = Loginfo()
    log.log_write('')
    log.log_close()
