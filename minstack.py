import heapq

class DoublyLinkedList(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy = DoublyLinkedList(0)
        self.dln = self.dummy
        self.temp = None
        # self.queue = []
        # self.heapq.heapify(queue)
        self.obj_map = {}
        

    def push(self, x: int) -> None:
        self.dln.next = DoublyLinkedList(x)
        self.obj_map[self.dln.next] = x
        # self.queue.push(x)
        self.temp = self.dln
        self.dln = self.dln.next
        self.dln.prev = self.temp
        self.dummy.prev = self.dln
        
        
    def pop(self) -> None:
        
        del self.obj_map[self.dln]
        self.dln = self.dln.prev
        self.dln.next = self.dln.next.next



    def top(self) -> int:
        return self.dln.val;
        
    def getMin(self) -> int:
        return min(self.obj_map.values());


        # min_val = float('inf')
        # self.min_dummy = self.dummy
        # self.min_dummy = self.min_dummy.next
        # while self.min_dummy:
        #     min_val = min(min_val, self.min_dummy.val)
        #     self.min_dummy = self.min_dummy.next
        # return min_val;

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.push(0)
print(obj.getMin())
# print(obj.top())
obj.pop()
print(obj.getMin())
# print(obj.top())
obj.pop()
print(obj.getMin())
# print(obj.top())
obj.pop()
# print(obj.top())
print(obj.getMin())

