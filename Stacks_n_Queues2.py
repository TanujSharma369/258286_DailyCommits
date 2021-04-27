#inbuild libraries
from collections import deque

#creating object of deque class
my_queue = deque()

#appending into queue
my_queue.append(5)
my_queue.append(6)
my_queue.append(7)
my_queue.append(8)

#displaying queue
print(my_queue)

#poping from the queue
print(my_queue.popleft())
print(my_queue.pop())


