class UnsortedArrayMap:
    class item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value

    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        pass

    def __getitem__(self, key):
        for item in self.data:
            if item.key == key:
                return item.value
        raise Exception("Key Error:" + str(key))

    def __delitem__(self, key):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass
