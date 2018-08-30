# A node class to create node elements
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkList :
    def __init__(self):
        self.head = None

    # To traverse the list
    def traverse(self):
        current_node = self.head
        while(current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    # To insert a node at the begining
    def insert_at_beg(self, new_node):
        new_node.next = self.head
        self.head = new_node

    # To insert a node at the end
    def insert_at_end(self, new_node_end):
        # If list is empty
        if self.head is None:
            self.head = new_node_end
        # If list is not empty
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = new_node_end

    # To insert after a given node
    def insert_at_pos(self, data_to_insert, after_data):
        new_node = Node(data_to_insert)
        temp = self.head
        while(temp is not None):
            if(temp.data == after_data):
                new_node.next = temp.next
                temp.next = new_node
                break
            else:
                temp = temp.next

    # To delete given a key
    def delete_at_key(self,key):
        temp = self.head # To temporary store the head
        # To check if first node is to delete
        if (temp.data == key):
            self.head = self.head.next
            temp = None
            return
        # Traverse the LL to find the node to be deleted
        while(temp is not None):
            if temp.data == key :
                break
            prev = temp
            temp = temp.next
        # If key value is not present in LL
        if(temp == None):
            print("Key value is not present")
        else:
            prev.next = temp.next
            temp = None

    # Delete LL
    def delete_ll(self):
        temp = self.head
        while(temp):
            prev = temp
            temp = temp.next
            del prev.data

    # To find the length of link list
    def len_of_ll(self):
        count = 0 # To count the number of elements
        temp = self.head # To store the head of LL
        while(temp):
            count+=1 # for every element increase the counter
            temp=temp.next # to move to the next element
        return count

    # To find middle of the link list
    def middle_of_ll(self):
        temp = self.head # To temp store the head
        counter = sllist.len_of_ll() # To get the length of the LL
        middle_pos = counter // 2 # To get the integer value of the middle of the LL
        pos = 0 # To iterate the variable till the middle_pos
        while(temp is not None):
            if(pos == middle_pos):
                print("Middle element is:", temp.data)
                # Break the loop once you reach the middle element
                break
            else:
                temp = temp.next # To move to the next element
                pos += 1 # to increment the pos

    # Faster method to find middle element of LL
    def midd_of_ll_fast(self):
        sl_pointer = self.head
        fast_pointer = self.head
        while(fast_pointer.next):
            sl_pointer = sl_pointer.next
            fast_pointer = fast_pointer.next.next
        print("Middle of the element is:", sl_pointer.data)

    # To find loop in LL and count the length of the loop
    def detect_loop_ll_count(self):
        sl_pointer = self.head
        fast_pointer = self.head
        counter = 0
        while(fast_pointer.next):
            sl_pointer = sl_pointer.next
            fast_pointer = fast_pointer.next.next
            counter+=1
            if(sl_pointer.data == fast_pointer.data):
                return True, counter
        return False

    # To reverse LL
    def reverse_ll(self):
        #define the 3 pointers
        prev_node = None
        curr_node = self.head
        next_node = None
        while(curr_node):
            #before changing the next of current, store it
            next_node = curr_node.next
            # to store the address of its previous node
            curr_node.next = prev_node
            # move both the curr and prev
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


if __name__ == "__main__":
    # To create object of Singlelist class
    sllist = SingleLinkList()
    # To create 3 Nodes from the Node class
    first = Node(100)
    second = Node(200)
    third = Node(300)
    new_node = Node(400)
    new_node_end = Node(500)
    sllist.head = first
    first.next  = second
    second.next = third
    third.next = new_node
    new_node.next = new_node_end
    #new_node_end.next = second
    #sllist.traverse()
    #sllist.insert_at_beg(new_node)
    #sllist.insert_at_end(new_node_end)
    #sllist.insert_at_pos(500, 200)
    #sllist.delete_at_key(500)
    #sllist.delete_ll()
    # len_ll = sllist.len_of_ll()
    #print("Length of the LL: ", len_ll)
    #sllist.middle_of_ll()
    #sllist.midd_of_ll_fast()
    #result =[]
    #result = sllist.detect_loop_ll_count()
    #print("loop in LL is", result)
    print("Print the linked list")
    sllist.traverse()
    sllist.reverse_ll()
    print("Print the reversed linked list")
    sllist.traverse()

