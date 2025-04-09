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