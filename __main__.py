from StacksQueues import *


def main():
    print("Stack")
    a = LinkedListStack()
    a.append(10)
    a.append(20)
    a.append(30)
    print(len(a))
    print(a)
    print(a.top())
    print(a.first())
    print(a.last())
    a.pop()
    print(a)

    print("Queue")
    a = LinkedListQueue()
    a.append(10)
    a.append(20)
    a.append(30)
    print(len(a))
    print(a)
    print(a.top())
    print(a.first())
    print(a.last())
    a.pop()
    print(a)
    #
    print("DeQueue")
    a = LinkedListDeque()
    a.append(10)
    a.append(20)
    a.append(30)
    a.insert(25)
    print(len(a))
    print(a)
    a.append_left(5)
    print(a)
    a.pop()
    print(a)
    a.pop_left()
    print(a)
    return

if __name__ == "__main__":
    main()
