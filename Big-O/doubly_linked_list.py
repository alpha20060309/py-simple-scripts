#Doubly linked lists

class DoublyNode:
    def __init__(self , value , next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)

Head = tail = DoublyNode(1)
print(tail)

# Display - O(n)
def display(head):
    curr = head
    elements = []

    while curr:
        elements.append(str(curr.value))
        curr = curr.next

    print(" <-> ".join(elements))

display(Head)

#Insert at the beginning - O(n)
def insert_at_the_beginning(head,tail,val):
    new_node = DoublyNode(val,next=head)
    head.prev = new_node

    return new_node,tail

Head,tail = insert_at_the_beginning(Head,tail,5)
display(Head)


def insert_at_the_end(head,tail,val):
    new_node = DoublyNode(val,prev=tail)
    tail.next = new_node

    return head,new_node

Head,tail = insert_at_the_end(Head,tail,10)
display(Head)

