class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DynamicStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.stack_size()<100:
            node=Node(data)
            temp = self.head
            node.next=temp
            self.head=node
            del temp
        else:
            print ("OverFlow")

    def pop(self):
        if self.is_empty():
            print ("UnderFlow")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            del temp
    def stack_size(self):
        i=0
        current_node=self.head
        while current_node is not None:
            current_node=current_node.next
            i+=1
        return i
    def peek(self):
        if  self.is_empty():
            print("the stack is empty")
        else:
            print(self.head.data)
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

# At the first glance the stack box has ninety-five (95) books,
book_shelf = DynamicStack()
for i in range(95):
    book_shelf.push("first_book"+str(i+1))

# A. Tesfay adds three books one by one with ID=369, 248, 460 and title = “book 1”, “book 2”, “book
# 3” respectively
book_shelf.push("book 1")
book_shelf.push("book 2")
book_shelf.push("book 3")
# B. Weini takes one book from the stack box to the book shelf.
book_shelf.pop()
# C. Gebrekidan looks at the top element and shows the total number of books on the stack box.
book_shelf.peek()
# D. Weini takes one book from the stack box to the book shelf
book_shelf.pop()
# E. Tesfay adds four books to the stack box with ID = 142, 364, 576, and 798 and title “book 4”, “book
# 5”, “book 6”, and “book 7” respectively.\
book_shelf.push("book 4")
book_shelf.push("book 5")
book_shelf.push("book 6")
book_shelf.push("book 7")
# book_shelf.print_stack()
# F. Gebrekidan looks at the top element and shows the total number of books on the stack box
book_shelf.peek()
print (book_shelf.stack_size())
# G. Tesfay adds one book to the stack box with ID = 111 and title = “book 8”
book_shelf.push("book 8")
# H. Gebrekidan looks at the top element and shows the total number of books on the stack box.
book_shelf.peek()
print (book_shelf.stack_size())
# I. Weini takes hundred books one by one from the stack box to the book shelf.
for i in range(100):
    book_shelf.pop()
# J. Gebrekidan looks at the top element and shows the total number of books on the stack box.
book_shelf.peek()
print (book_shelf.stack_size())

# book_shelf.print_stack()
# K. Weini takes one book from the stack box to the book shelf.
book_shelf.pop()
book_shelf.print_list()
