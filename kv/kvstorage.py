from pysyncobj import SyncObj, SyncObjConf, replicated


class KVStorage(SyncObj):
    def __init__(self, selfAddress, partnerAddrs):
        conf = SyncObjConf()
        super(KVStorage, self).__init__(selfAddress, partnerAddrs, conf)
        self.__data = {}

    @replicated
    def put(self, key, value):
        print("put key: ", key, " with value: ", value)
        self.__data[key] = value

    @replicated
    def append(self, key, value):
        print("append key: ", key, " with value: ", value)
        if key in self.__data:
            self.__data[key].append(value)
        else:
            self.__data[key] = [value]

    def get(self, key):
        print("get key: ", key)
        return self.__data.get(key, None)

    def get_dumpfile(self):
        return self.dumpFile
