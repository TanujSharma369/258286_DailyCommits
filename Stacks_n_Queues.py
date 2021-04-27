# creating a wrapper class for stack operations
class Stack:
    def __init__(self):
        self.stack = list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return "Under flow"
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return "Empty Stack"
    def __str__(self):
        return str(self.stack)

#creating object of stack class
my_stack = Stack()

#pushing into stacks
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

#printing stack
print(my_stack)

#poping form stack
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())