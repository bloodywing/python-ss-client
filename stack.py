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
            if(_use_hash == True):
                _list.append(item.__hashCode)
            else:
                _list.append(item)

        _list[_max:] = []

    def remove(self, item):
        if(self.contains(item) == True):
            pass

    def contains(self, item):
        if(_use_hash == True):
            return item.__hashCode in _list
        else:
            return item in _list
