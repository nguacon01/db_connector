from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
import os

from .engine import Engine
from .base_model import Model
from .configuration import Config

class db_connector(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.Model = Model
        self.Base = declarative_base()
        self.session()

    @property
    def config(self):
        if not os.path.isfile(self.config_file_path):
            raise IOError('Config file not accessible')
        return Config(self.config_file_path).ConfMap

    @property
    def engine(self):
        return Engine(self.config).engine

    # @property
    def session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    @property
    def inspector(self):
        return inspect(self.engine)
    
    def create_all(self):
        return self.Base.metadata.create_all(self.engine)
    def drop_all(self):
        return self.Base.metadata.drop_all(self.engine)

    def __repr__(self):
        return f"{self.config_file_path}"
    
    def get_schemas(self):
        return self.inspector.get_schema_names()
    
    def get_all_table_names(self):
        table_names = []
        schemas = self.get_schemas()
        for schema in schemas:
            print("schema: %s" % schema)
            print("*"*50)
            for table_name in self.inspector.get_table_names(schema=schema):
                print(f'table: {table_name}')
                table_names.append(table_name)
        return table_names