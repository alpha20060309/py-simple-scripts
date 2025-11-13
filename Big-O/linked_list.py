# Singly linked lists

class SinglyNode:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

    def __str__(self):
        return str(self.value)


Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

#Traverse the list - O(n)

curr = Head

while curr:
    print(curr)
    curr = curr.next

#Display the linked lists - O(n)

def display(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)

def search(head, val):
    curr = head
    while curr:
        if val == curr.value:
            print('Found')
            return True
        curr = curr.next

    print('Not Found')
    return False

search(Head,7)