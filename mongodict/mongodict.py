import collections


class MongoDict(collections.MutableMapping):
    """A dictionari to store and retrive data to the Mongodb.
    """
    def __init__(self, *args, **kwargs):
        if 'collection' in kwargs:
            collection = kwargs['collection']
            del kwargs['collection']
        else:
            raise Exception('You mast pass the collection by collection '
                            'keyword')
        #self.store = mdbpool.get_collection(collection)
        self.store = collection
        self.store.ensure_index('id', unique=True, cache_for=300)
        self.update(dict(*args, **kwargs))

    def __getitem__(self, item):
        x = self.store.find_one({'id': item})
        if not x:
            raise KeyError()
        else:
            return x['value']

    def __setitem__(self, key, value):
        x = self.store.find_one({'id': key})
        if x:
            self.store.update({'id': key}, {'$set': {'value': value}})
        else:
            self.store.insert({'id': key, 'value': value})

    def __delitem__(self, key):
        self.store.remove({'id': key})

    def __iter__(self):
        return iter(self.store.find())

    def __len__(self):
        return self.store.find().count()