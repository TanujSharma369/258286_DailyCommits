"""
PTR
value at parent node > value at child node
parent node = position/2
left child = position*2
right child = position*2+1
"""
class MaxHeap:
    def __init__(self,items = []):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1)

    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1,len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i] , self.heap[j] = self.heap[j] , self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <=1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = right
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)
    def __str__(self):
        return str(self.heap)


m = MaxHeap([3,95,21,56])
m.push(10)
print(m)
print(m.peek())
print(m.pop())
print(m)