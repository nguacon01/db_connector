import configparser
import os

class Config(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
    
    @property
    def config(self):
        config = configparser.ConfigParser()
        # prevent configparser convert all config keys to lower key
        config.optionxform = str
        config.read(self.config_file_path)
        return config

    @property
    def ConfMap(self):
        config_mapper = {}
        for section in self.config.sections():
            section_dict = {}
            for key, val in self.config.items(section):
                section_dict[key] = val
                config_mapper[str(section)] = section_dict

        if 'ENV' in os.environ and os.environ['ENV'].lower() == 'production':
            return config_mapper['PROD']
        return config_mapper['DEV']

    def getValue(self, key):
        value = ''
        try:
            value = self.ConfMap[key]
        except KeyError as key:
            print('Key ' + key + ' did not found in config file')
        return value

    def __resp__(self):
        return f"<Config: {self.config_file_path}>"

    __str__ = __resp__