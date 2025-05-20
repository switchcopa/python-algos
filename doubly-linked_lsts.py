class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data 

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        if self.head is None:
            new_node = Node(data=data)
            self.head = new_node
            self.tail = new_node
            return 

        new_node = Node(next=self.head, data=data)
        self.head.prev = new_node
        self.head = new_node

    def output_front(self):
        if self.head is None:
            print("List is empty")
            return 
        
        node = self.head
        s = ""

        while node:
            s += str(node.data) + " -> "
            node = node.next 
        print(s + "NULL")

    def output_back(self):
        if self.head is None:
            print("List is empty")
            return 
        
        node = self.tail
        s = ""
        
        while node:
            s += " <- " + str(node.data)
            node = node.prev

        print("NULL" + s)

    def get_length(self):
        count = 0 
        node = self.head 
        while node:
            node = node.next 
            count += 1 

        return count 

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return 

        node = self.head

        while node.next:
            node = node.next 

        new_node = Node(node, None, data)
        node.next = new_node
        self.tail = new_node

    def insert_at_index(self, data, index):
        length = self.get_length()

        if length < index:
            raise IndexError("list index out of range")
        
        if length == index:
            self.insert_at_end(data)
            return 
        
        if index == 0:
            self.insert_at_beginning(data)
            return 

        node = self.head
        count = 0

        while count < index - 1:
            node = node.next 
            count += 1 

        new_node = Node(node, node.next, data)
        node.next.prev = new_node
        node.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            return 
        
        if not self.head.next:
            self.head = None 
            self.tail = None 
            return 
        
        new_head = self.head.next
        self.head = new_head
        new_head.prev = None 

    def delete_at_end(self):
        if self.head is None:
            return 
        
        if not self.head.next:
            self.head = None 
            self.tail = None 
            return 
        
        new_tail = self.tail.prev 
        self.tail = new_tail 
        new_tail.next = None 

    def insert_values(self, values):

        for x in values:
            self.insert_at_end(x)

    def delete_at_index(self, index):
        length = self.get_length()

        if length < index:
            raise IndexError("list index out of range")
        
        if length == index:
            self.delete_at_end()
            return 
        
        if index == 0:
            self.delete_at_beginning()
            return 
        
        count = 0 
        node = self.head 

        while count < index - 1:
            count += 1 
            node = node.next 

        temp = node.next.next 
        node.next = temp 
        
        if temp:
            temp.prev = node 

    def lookup(self, data):
        if self.head is None:
            return 
        
        node = self.head 
        index = 0 

        while node:
            if node.data == data:
                return index 
            
            node = node.next 
            index += 1 

        return False

    def lookup_all(self, data):
        result = []
        node = self.head 
        index = 0

        while node:
            if node.data == data:
                result.append(index)

            node = node.next  
            index += 1 

        return result if result else False

    def delete_by_data(self, data):
        if self.head is None:
            return 

        while self.head and self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None 

        node = self.head
        while node and node.next:
            if node.next.data == data:
                temp = node.next.next 
                node.next = temp 
            else:
                node = node.next 
        
        return self.head 
    
    def reverse(self):
        if self.head is None:
            return 
        
        curr = self.head 
        prev = None 
        
        while curr:
            temp = curr.next
            curr.next = prev
            curr.prev = temp 
            prev = curr
            curr = temp

        self.head, self.tail = self.tail, self.head 

if __name__ == '__main__':
    ll = doubly_linked_list()
    ll.insert_values([9,9,8,1]) 
    ll.output_back()
    ll.output_front() 
    ll.reverse()
    ll.output_back()
    ll.output_front()