class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    # some_var = [] созданная здесь переменная будет указывать на один и тот же объект в памяти
    
    def __init__(self, value = 0):
        self.start = ListNode(value)
        self.last = self.start
        self.length = 1
        self.current = self.start

    def len(self):
        return self.length

    def get(self,key):
        i = 0
        cur_node = self.start 
        while (i < key):
            cur_node = cur_node.next
            i+=1
        if cur_node is not None:
            return cur_node
        else:
            return 'out of range'

    def append(self, value):
        self.last.next = ListNode(value)
        self.last = self.last.next
        self.length += 1

    def pop(self):
        if self.length == 1:
            return "Don't touch it!"
        prev = self.start
        while(prev.next != self.last):
            prev = prev.next
        result = self.last
        self.length -= 1
        prev.next = None
        self.last = prev
        return result

    def __getitem__(self,key): # для вызова значения через []
        return self.get(key)

    def __next__(self): # для вызова следующего значения при итерировании
        result = self.current
        if self.current is None:
            raise StopIteration()
        self.current = self.current.next
        return result

    def __iter__(self):
        return self
    # def __setitem__(self, key, value) для задания значений через []

def test_generator(): # функция-генератор
    for i in range(5):
        yield i # похож на встроенный некст

print('generator')
for i in test_generator():
    print(i)

array = LinkedList(4)

array.append(5)

print(array.length)
print(array.get(0).val)
print(array.get(1).val)
print(array.length)
print(array[1].val)


print('Iterator')
for node in array:
    print(node.val)