import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        try:
            url=config.get('common info', 'baseUrl')
            return url
        except:
            assert False, "Config loading failed"

    @staticmethod
    def getBrowserName():
        try:
            browsername = config.get('common info', 'Browser')
            return browsername
        except:
            assert False, "Config loading failed"

    @staticmethod
    def getPassword():
        try:
            password = config.get('common info', 'password')
            return password
        except:
            assert False, "Config loading failed"
