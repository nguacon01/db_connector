# db_connector
A module to help us to connect to a db, create tables and do some queries. This module use SqlAlchemy
### Connect to a database
'''python
import db_connector
db = db_connector('/path/to/your/ini/config/file.ini')
'''

### create tables
'''python
from sqlalchemy import Column, String, Integer, Text, text
class NameOfYourTable(db.Model, db.Base):
  column1 = Column(Integer)
  column2 = Column(String(255))
  
  def __init__(self, column1, column2):
    self.column1 = column1
    self.column2 = column2

db.create_all()
'''
