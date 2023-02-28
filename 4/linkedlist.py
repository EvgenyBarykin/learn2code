# сами делаем список как в питоне
# один объект класса будет его узлом со ссылкой на следующий
class LinkedList:

# чтобы написать функцию которая ничего не делает можно написать pass

    def __init__(self) -> None:
        pass

    def len(self):
        pass

    def get(self,key):
        pass

    def append(self, value):
        pass

    def pop(self, value):
        pass

def get_item(linkedlist, key):
    i = 0
    cur_node = linkedlist 
    while (i < key):
        cur_node = cur_node.next
        i+=1
    if cur_node is not None:
        print(cur_node.val)
    else:
        print('out of range')

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node2 = ListNode(22)
node1 = ListNode(5, node2)

print(node1.val)
print(node1.next)

# f перед строкой - внутри нее в фигурных скобках можно использовать переменные
print(f'Next element value {node1.next.val}')

print(node2.val)
print(node2.next)

def get_last_node(linkedlist):
    last_node = linkedlist
    while(last_node.next != None):
        last_node = last_node.next
    return last_node

def append(linkedlist, value):
    new_node = ListNode(value)
    last_node = get_last_node(linkedlist)
    last_node.next = new_node

#class Solution(object):
#   def reverseList(self, head):

append(node1, 10)
print(node2.next.val)

simplelist = ListNode(1)
append(simplelist, 2)
append(simplelist, 5)
print(simplelist.val)
print(simplelist.next.val)
print(simplelist.next.next.val)

get_item(simplelist, 3)