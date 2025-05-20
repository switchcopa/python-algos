class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(None, data)
            self.head = new_node
            return 
        else:
            new_node = Node(self.head, data)
            self.head = new_node
        
    def get_length(self):
        count = 0 
        node = self.head
        while node.next:
            node = node.next
            count += 1

        return count 

    def output(self):
        if self.head is None:
            print("Linked list is empty")
            return 
        else:
            node = self.head 
            s = ""
            while node:
                s += str(node.data) + " -> "
                node = node.next
            print(s + "NULL")

    
    def insert_at_end(self, data):
        if not self.head:
            self.insert_at_beginning(data)
            return 
        else:
            node = self.head 
            while node.next:
                node = node.next
            
            new_node = Node(None, data)
            node.next = new_node
            
    def insert_at_index(self, index, data):
        length = self.get_length()

        if length < index:
            raise IndexError("index out of range")
        elif index == 0:
            self.insert_at_beginning(data)
            return 
        elif index == length:
            self.insert_at_end(data)
            return 
        
        node = self.head 
        count = 0 

        while count < index - 1:
            count += 1
            node = node.next

        new_node = Node(node.next, data)
        node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return 
        
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            return 
        
        node = self.head
        prev = None

        while node.next:
            prev = node
            node = node.next

        prev.next = None    

    def delete_at_index(self, index):
        if not self.head:
            return 
        
        if index == 0:
            self.delete_at_beginning()
            return 
        if index == self.get_length():
            self.delete_at_end()
            return 
        
        node = self.head
        count = 0 

        while count < index - 1:
            node = node.next
            count += 1 
        
        node.next = node.next.next

    def lookup(self, data):
        if self.head is None:
            return -1 # not found 
        
        node = self.head 
        index = 0
        while node:
            if node.data == data:
                return index
            index +=1 
            node = node.next

        return -1

    def lookup_all(self, data):
        indexes = []
        
        if self.head is None:
            return None

        index = 0 
        node = self.head 
        while node:
            if node.data == data:
                indexes.append(index)
                continue

            index += 1 
            node = node.next 

        return indexes if indexes else None

    def delete_by_data(self, data):
        if self.head is None:
            return 
        
        """
        This is my code that was wrong before:
        dummy = Node(data=0)
        dummy.next = self.head 
        node = dummy

        while node.next:
            if node.next.data != data:
                node = node.next 
                continue 

            node.next = node.next.next

        return dummy.next

        vs NOW:
        
        """

        while self.head and self.head.data == data:
            self.head = self.head.next 

        node = self.head 
        while node and node.next:
            if node.next.data == data:
                node.next = node.next.next
            else:
                node = node.next 

        return self.head

    def insert_values(self, values):
        for x in values:
            self.insert_at_end(x)

    def reverse(self):
        if self.head is None:
            return 
        
        curr = self.head 
        prev = None 

        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr 
            curr = temp 
        
        self.head = prev 

        return prev 
    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(1)
    ll.insert_at_end(3)
    ll.insert_at_end(7)
    ll.insert_at_index(3,11)
    ll.insert_at_beginning(3)
    ll.output()
    ll.delete_by_data(3)
    ll.output()
    
