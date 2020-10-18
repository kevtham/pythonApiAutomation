import configparser
import os


class TestConfig():

    def getURlname(key, value):
        print("Attempting to get the url name :::")
        urlname=None
        try:
            config = configparser.ConfigParser()
            configfile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'automation.cfg')
            config.read(configfile)
            urlname = config.get(key, value)
        except Exception as e:
            print("Value not found for Key : %s" %value)
        return urlname