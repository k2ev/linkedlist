import abc
from Nodes import *


class LinkedListSingly:
    __metaclass__ = abc.ABCMeta

    # implementation uses sentinel node for head
    def __init__(self):
        self._head = Node()  # head is sentinel node
        self._length = 0

    @abc.abstractmethod
    def append(self, item):
        # FIFO vs Stack can implement this differently
        return

    def pop(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            next_ = self._head.get_next()
            self._head = next_
            self._length -= 1
            return

    def __str__(self):
        current = self._head
        s, sep = "", "->"
        while current is not None:
            sep = "" if s == "" else "->"
            s += sep + str(current)
            current = current.get_next()
        return s

    def __len__(self):
        return self._length

    def is_empty(self):
        return len(self) == 0

    def __contains__(self, elem):
        current = self._head
        found = False
        while current is not None:
            if current.get_item() == elem:
                found = True
                break
            current = current.getNext()
        return found

    def top(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            return self._head.get_item()

    def remove(self, elem):
        curr_marker = self._head
        prev_marker = self._head
        flag_removed = False
        while not flag_removed and curr_marker is not None:
            if curr_marker.get_item() == elem:
                prev_marker.set_next(curr_marker.get_next())
                self._length -= 1
                flag_removed = True
                break
            prev_marker = curr_marker
            curr_marker = curr_marker.get_next()
        return flag_removed

    @abc.abstractmethod
    def first(self):
        return

    @abc.abstractmethod
    def last(self):
        return


class LinkedListStack(LinkedListSingly):
    # Stack or a LIFO implementation of singly linked list
    def __init__(self):
        super().__init__()

    def append(self, item):
        new_node = Node(item, self._head)
        self._head = new_node
        self._length += 1

    def first(self):
        current_node = self._head
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            next_node = current_node.get_next()
            while next_node is not None:
                current_node = next_node
                next_node = current_node.get_next()
            return current_node.get_item()

    def last(self):
        return self.top()


class LinkedListQueue(LinkedListSingly):
    # FIFO implementation of singly linked list
    def __init__(self):
        super().__init__()
        self._tail = None  # marker node

    def append(self, item):
        new = Node(item)
        current = self._tail
        if current is not None:
            current.set_next(new)
        else:
            self._head = new
        self._tail = new
        self._length += 1
        return True

    def first(self):
        return self.top()

    def last(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            return self._tail.get_item()


class LinkedListDeque:
    # uses sentinel nodes for head and tail
    def __init__(self):
        self._head = NodeDeque()
        self._tail = NodeDeque()
        self._head.set_next(self._tail)
        self._tail.set_prev(self._head)
        self._length = 0

    def append(self, item):
        next_node = self._head.get_next()
        new_node = NodeDeque(item)
        self._link_nodes(self._head, next_node, new_node)
        self._length += 1
        return

    def pop(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            current_node = self._head.get_next()
            next_node = current_node.get_next()
            self._link_nodes(self._head, next_node)
            return

    def append_left(self, item):
        prior_node = self._tail.get_prev()
        new_node = NodeDeque(item)
        self._link_nodes(prior_node, self._tail, new_node)
        self._length += 1
        return

    def pop_left(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            current_node = self._tail.get_prev()
            prev_node = current_node.get_prev()
            self._link_nodes(prev_node, self._tail)
            return

    def _link_nodes(self, node_prev, node_next, node_curr=None):
        if node_curr is None:
            node_prev.set_next(node_next)
            node_next.set_prev(node_prev)
        else:
            self._link_nodes(node_prev, node_curr)
            self._link_nodes(node_curr, node_next)
        return

    def top(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            current_node = self._head.get_next()
            return current_node.get_item()

    def top_left(self):
        if self.is_empty() is True:
            raise ValueError("Empty Stack or Queue")
        else:
            current_node = self._tail.get_prev()
            return current_node.get_item()

    def __str__(self):
        current = self._tail.get_prev()
        s = ""
        while current is not self._head:
            sep = "->" if current.get_prev() is not self._head else ""
            s += str(current) + sep
            current = current.get_prev()
        return s

    def __len__(self):
        return self._length

    def is_empty(self):
        return len(self) == 0

    def __contains__(self, elem):
        current = self._head.get_next()
        found = False
        while current is not self._tail:
            if current.get_item() == elem:
                found = True
                break
            current = current.get_next()
        return found

    def insert(self, item):
        current_node = self._head.get_next()
        new_node = NodeDeque(item)
        flag_insert = False
        while not flag_insert and current_node is not self._tail:
            if new_node < current_node:
                self._link_nodes(current_node, current_node.get_next(), new_node)
                flag_insert = True
            current_node = current_node.get_next()
        return flag_insert
