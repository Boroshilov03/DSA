#Push and Pop element : O(1)
#Search element by value: O(n)

#Ex: Undo (Ctrl+Z), When visiting websites (history)

#stk = deque()
#stk.append(5)
#stk.append(9)
#stk.pop()


s = []
#problem with array is you have to allocate memory when you ran out space &
# also copying these items into new list
s.append('1st Website')
s.append('2st Website')
s.append('3st Website')
# print(s)
# print(s.pop())

#Using deque rids of that problem bcz it grows dynamically.

from collections import deque
# stack = deque()
# dir(stack) #shows all the functions available
#
# stack.append("1st Website")
# stack.append("2st Website")
# stack.append("3st Website")
# print(stack)
# print(stack.pop())

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()  # Return the popped value

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ""
    while not stack.is_empty():
        rstr += stack.pop()

    return rstr

print(reverse_string("We will conquer COVI-19"))
print(reverse_string("I am the king"))
