## This file contains my observations and notes about Linked Lists
## I have also created my own Linked List Class to understand the DS

## Observations

## Linked Lists(LL) do not have indexes.
## LL is a type of list that is in a contiguous place in memory, as in, all elements are all right next to each other in memory.
## With a LL all the nodes are going to be spread all over the place.

## Also with a LL there is a variabled called head which points to the first node in a LL
##   head                tail
##    |                    |
##   (1) -> (2) -> (3) -> (4) -> None (null)

## Big O logic to remember when dealing with LL

## When adding a node (append function) to the end of the list
##   head                tail
##    |                    |
##   (1) -> (2) -> (3) -> (4) -> None (null)           (5) -> None
## What happens with this function is that the last node within the last points to the new node, and than we make tail point to the new node also
##   head                       tail
##    |                           |
##   (1) -> (2) -> (3) -> (4) -> (5) -> None
## Given this understanding, we label the time complexity for this operation as O(1), the main reason being it doesn't matter how big the LL is.
## The number of operations to add a new node to the end of a list will stay the same.
## Adding a node to the front of the list will result in a similar time complexity of O(1); logically it's the same as the explanation above.
## Removing a node from the front of the list is very similar to the two examples mentioned above. Time Complexity: O(1).

## When removing a node from the end of the list, it is a bit more complicated. The variable tail will need to point to a node right
## before the end of the node. In order to retrieve this information, we would need to make tail equal to the pointer that points
## to that second last node. 
##   head                                       tail
##    |                                          |
##   (1) -> (2) -> (3) -> (4) -> ?              (5) -> None
##                     |   |                     |
##                     | to be new end        to remove
##                  this pointer will be set to equal tails
## In order to get to the new end, we have to start at the head node, and iterate through the list until we get to the pointer that points
## to the new end. Since we had to iterate through the entire list to make this operation work, the time complexity is O(n).

## When adding an item to the middle of the list, we would need to find the pointer that points towards our desired location.
##   head                 tail
##    |                    |
##   (1) -> (2) -> (3) -> (4) -> None              (5) -> None
##                                                  |
##                                                to add
## Suppose we wanted to add Node 5 in between node 3 and 4. What we would need to do is iterate from the head node until we get to node 3. 
## Than we would take the pointer pointing to node 4 and make that equal to what node 5 points to. Then, we make Node 3 point to Node 5
##   head                        tail
##    |                           |
##   (1) -> (2) -> (3) -> (5) -> (4) -> None             
## Since we had to iterate through the list, this also has a time complexity of O(n).

## Now suppose we wanted to remove node 5. It's pretty much the same process, start at head node and iterate through the list until we get
## to the desired node. From there, what we would do is make node 3 pointer equal to what node 5 is pointing to next. Than from there, we
## make node 5 point to None (null).
## Just like before, since we iterate from the head to the desired to the node the time complexity is O(n).
## When comparing LL to normal lists, you can just look up the index with a value of 4, making this operation O(1) 
## when using a normal list vs a LL.

## Simple helper class; creates a node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
## Main LinkedList
class LinkedList:
    # LL Constructor
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    ## Simple print function
    def printList(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        ## First we will have to create a new node
        new_node = Node(value)
        ## edge case what if there is no list?
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
        ## adding a new node to the list
            self.tail.next = new_node
            self.tail = new_node
        ## incrementing by 1
        self.length += 1
        ## Not needed for the append method, just for testing purposes I am returning a bool
        return True
    
    def pop(self):
        ## Edge Case: Empty List
        if self.length == 0:
            return None
        ## Need two variables to track the current and previous node
        temp = self.head
        pre = self.head
        ## iterate through the list until temp.next is None, ensuring pre stops at the second last node
        while(temp.next):
            pre = temp
            temp = temp.next
        ## removing the last node
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        ## if the remaining list is now empty
        if self.length == 0:
            self.head = None
            self.tail = None
        ## returning the node we just removed
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        ## If the list is empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
        ## items in the list
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        ## Not needed for the prepend method, just for testing purposes I am returning a bool
        return True
        
    def pop_first(self):
        ## edge case if list is empty
        if self.length == 0:
            return None
        ## assigning temp variable to first node
        temp = self.head
        ## moving the head pointer to the second node
        self.head = self.head.next
        ## original first node now points to none
        temp.next = None
        self.length -= 1
        ## edge case if new list is empty, than we must return none
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        ## first we need to test if index is a valid number 
        if index < 0 or index >= self.length:
            return None
        ## variable to point to head
        temp = self.head
        ## the underscore (_) represents an unused variable
        ## for example normally you would label _ i, since
        ## we don't use i in the for loop, we replace i with _
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        ## get the node that the index is at
        temp = self.get(index)
        ## if the temp index is valid
        if temp is not None:
            ## change the value
            temp.value = value 
            ## return true
            return True
        return False
    
    def insert(self, index, value):
        ## if the index is negative or outside of the scope we return false
        if index < 0 or index > self.length:
            return False
        ## if the index selected is for the first node we use the prepend func
        if index == 0:
            return self.prepend(value)
        ## if the index selected is for the last node we use the append func
        if index == self.length:
            return self.append(value)
        ## creating a new node
        new_node = Node(value)
        ## need a variable pointing to the node before the area we need to insert
        temp = self.get(index - 1)        
        ## assigning new node to the next node in the list
        new_node.next = temp.next
        ## assigning previous node to the new node
        temp.next = new_node
        self.length += 1
        return True

## Creating a new LL
my_linked_list = LinkedList(4)

print("Testing out Print Functionality:")
## Testing Print
my_linked_list.printList()

print("")

print("Testing out Append Functionality:")
## Testing Append function
my_linked_list.append(2)
my_linked_list.printList()

print("")

print("Testing out Pop Functionality:")
## Testing Pop function
my_linked_list.pop()
my_linked_list.printList()

print("")

print("Testing out prepend Functionality:")
## Testing prepend function
my_linked_list.prepend(1)
my_linked_list.printList()

print("")

print("Testing out pop_first Functionality:")
## Testing pop_first function
my_linked_list.pop_first()
my_linked_list.printList()

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(5)
my_linked_list.append(6)

print("")
print("New List")
my_linked_list.printList()

print("")

print("Testing out get Functionality by returning second node:")
## Testing get function
print(my_linked_list.get(1).value)

print("")

print("Testing out set Functionality by changing value of first node to 1:")
## Testing get function
my_linked_list.set_value(0, 1)
my_linked_list.printList()

print("")

print("Testing out insert Functionality by inserting value 7 in between the first and second node:")
## Testing get function
my_linked_list.insert(1, 7)
my_linked_list.printList()
