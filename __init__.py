from .engine import Engine
from .base_model import Model
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import inspect

class db_connector(object):
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.engine = Engine(self.config_file_path).engine
        self.Model = Model
        self.Base = declarative_base()
        __Session = sessionmaker(bind=self.engine)
        self.session = __Session()
        self.inspector = inspect(self.engine)
    
    def create_all(self):
        return self.Base.metadata.create_all(self.engine)

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