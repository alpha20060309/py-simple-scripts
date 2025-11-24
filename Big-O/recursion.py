# Fibonacci
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)

def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

print(F(12))

# Linked list

class SinglyNode:

    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)


Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

Head.next = A
A.next = B
B.next = C


print(Head)

# Time Complexity: O(n)
# Space Complexity: O(n)
def reverse(node):
    if not node:
        return
    reverse(node.next)

    print(node)

reverse(Head)