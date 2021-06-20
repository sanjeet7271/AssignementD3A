import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        try:
            url=config.get('common info', 'baseUrl')
            return url
        except FileNotFoundError:
            assert False, "Config loading failed"

    @staticmethod
    def getBrowserName():
        try:
            browser_name = config.get('common info', 'Browser')
            return browser_name
        except FileNotFoundError:
            assert False, "Config loading failed"

    @staticmethod
    def getPassword():
        try:
            password = config.get('common info', 'password')
            return password
        except FileNotFoundError:
            assert False, "Config loading failed"
