# Node with single link
class Node:
    def __init__(self, item=None, next_=None):
        self._item = item
        self._next = next_

    def get_item(self):
        return self._item

    def get_next(self):
        return self._next

    def set_item(self, item):
        self._item = item
        return True

    def set_next(self, next_):
        self._next = next_
        return

    def __str__(self):
        return str(self.get_item())

    def __eq__(self, other):
        return self.get_item() == other.get_item()

    def __ne__(self, other):
        return self.get_item() != other.get_item()

    def __lt__(self, other):
        return self.get_item() < other.get_item()


class NodeDeque(Node):
    def __init__(self, item=None, next_=None, prev=None):
        super().__init__(item, next_)
        self._prev = prev

    def get_prev(self):
        return self._prev

    def set_prev(self, prev):
        self._prev = prev
        return
