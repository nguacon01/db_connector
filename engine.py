from sqlalchemy import create_engine
from .configuration import Config

class Engine:
    """
        create engine to connect to a database based on the config
        by default, engine uses the dev configs from config object
    """
    def __init__(self, config:dict):
        self.config = config

    @property
    def engine(self):
        """
            create engine, connect to the database
        """
        # by defautl, if there is no type of your db, it will be mysql
        db_type = self.config.get('SQL_TYPE_DB', 'mysql').lower()

        db_list = {
            'mysql':'mysql+pymysql',
            'postgres':'postgresql'
        }

        return create_engine(
                    f"{db_list[db_type]}://{self.config['SQL_USER']}:{self.config['SQL_PASSWORD']}@{self.config['SQL_HOST']}:{self.config['SQL_PORT']}/{self.config['SQL_DATABASE']}",
                    # echo=True
                )

    def __repr__(self):
        # return str(self.config)
        return f"<Engine:{self.config['SQL_USER']} - {self.config['SQL_HOST']} - {self.config['SQL_DATABASE']}"

    __str__ = __repr__