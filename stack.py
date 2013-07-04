class Stack:
    _list = []
    _use_hash = False
    _max = 2000

    def __init__(self, use_hash=False, max=2000):
        self._list = []
        self._use_hash = use_hash
        self._max = max

    def add(self, item):
        if(self.contains(item) == False):
            if(self._use_hash == True):
                self._list.append(item['__hashCode'])
            else:
                self._list.append(item)

        self._list[self._max:] = []

    def remove(self, item):
        if(self.contains(item) == True):
            pass

    def contains(self, item):
        x = None

        if(self._use_hash == True):
            x = item['__hashCode']
        else:
            x = item

        return x in self._list
