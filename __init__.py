from .engine import Engine
from .base_model import Model
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class db_connector(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.engine = Engine(self.config_file_path).engine
        self.Model = Model
        self.Base = declarative_base()
        __Session = sessionmaker(bind=self.engine)
        self.session = __Session()
    
    def create_all(self):
        return self.Base.metadata.create_all(self.engine)

    def __repr__(self):
        return f"{self.config_file_path}"