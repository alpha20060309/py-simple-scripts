# Stacks - Last In First Out (LIFO)

stk = []
print(stk)

# Append to top of stack - O(1)
stk.append(1)
stk.append(2)
stk.append(3)

print(stk)

# Pop from top of stack - O(1)
x = stk.pop()
print(x)
print(stk)

# Ask what is on top of stack - O(1)
print(stk[-1])


# Chekc stack is empty - O(1)
if stk:
    print(True)



# Queues - First In First Out (FIFO)

from collections import deque

q = deque()

print(q)

# Enqueue - Add element to the right - O(1)

q.append(5)
q.append(6)
q.append(7)

print(q)

# Dequeue - Remove element from left - O(1)

x = q.popleft()

print(x)

# Peek from left side - O(1)

print(q[0])