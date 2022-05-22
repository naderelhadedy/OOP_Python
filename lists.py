# the base class
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"


# the subclass
class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


# the subclass
class IntList(SimpleList):
    def __init__(self, items=()):
        for val in items: self._validate(val)
        super().__init__(items)

    @staticmethod
    def _validate(val):
        if not isinstance(val, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    pass
