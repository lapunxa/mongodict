mongodict
=========

Access Mongodb collections as Python dictionaries


```python
from pymongo import Connection
from pymongo.database import Database
from mongodict import MongoDict

connection = Connection()
db = Database(connection, 'mongo_test')
d = MongoDict(collection=db.d)
d['foo'] = 'bar'
d['niu'] = 'nau'
```