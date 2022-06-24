from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect
import os
<<<<<<< HEAD
=======

from .engine import Engine
from .base_model import Model
from .configuration import Config
>>>>>>> 9165280b192328e8aa8b137ded93b6c8c1c82998

class db_connector(object):

    def __init__(self, config_file_path, show_query=False, env_variable_key='ENV', env_variable_value='production'):
        self.env_variable_key = env_variable_key
        self.env_variable_value = env_variable_value
        self.show_query = show_query
        self.config_file_path = config_file_path
<<<<<<< HEAD
        self.engine = Engine(config_file_path=self.config_file_path,echo=self.show_query, env=self.get_env()).engine
        self.Model = Model
        self.Base = declarative_base()
        __Session = sessionmaker(bind=self.engine)
        self.session = __Session()
        self.inspector = inspect(self.engine)

    def get_env(self):
        if not self.env_variable_key or not self.env_variable_value:
            return 'DEV'
        if os.environ.get(self.env_variable_key, 'DEV') == self.env_variable_value:
            return 'PROD'
        return 'DEV'
=======
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
>>>>>>> 9165280b192328e8aa8b137ded93b6c8c1c82998
    
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