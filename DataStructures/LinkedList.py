class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_List(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end="  ")
                n = n.ref

    def add_begin(self, data):

        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # def add_after(self, data, new_data):
    #     n = self.head
    #     while n is not None:
    #         if new_data == n.data:
    #             break
    #         n = n.ref
    #     if n is None:
    #         print("node is not prsesent in LL")
    #     else:
    #         new_node = Node(data)
    #         new_node.ref = n.ref
    #         n.ref = new_node


LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
LL1.add_end(1000)
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_begin(50)
LL1.add_end(2000)
# LL1.add_after(1000, 2000)
LL1.print_List()
