'''
linked lists:
dynamic, versus array which is static
head, first value
middle, values
tail, last value
class Node
    self.next = next
    self.next = next
class LinkedList
    self.head = head_node
    self.tail = tail_node
arrows in linked list refer to a direction
nodes can't go against direction
each node is only able to refer to the next node

inserting into a linked list:
wrap value in a new linked list node
in this example, adding to end
have it point to none
previous tail point to new node we just made
update linked list tail reference

questions:
what does an empty linked list look like? a linked list with only one element?
how would you add to it?
how would you iterate along a linked list to reach an element that isn't the head or tail of the list?
how would you delete an element from a linked list

pros and cons:
pro, easier to insert and delete from the middle of a linked list compared to an array
pro, linked lists do not need to be allocated memory up front, less overhead
con, linked lists are not as cache-friendly since caches are typically optimized for contiguous memory accesses

QUEUE:
serialize data
achieve FIFO ordering
class Queue:
    self.size = 0
    self.storage = storage_data_structure
    underlying data structure to facilitate FIFO

questions:
what's the opposite of FIFO?
what data structure would you use to implement a queue?
when is FIFO useful and when is it not?

pros:
queues are simple and intuitive to use and implement
the can be used to serialize data coming in from multiple sources

con:
are not general purpose at all in and of themselves

LINKED LIST:
time complexity to find an index in an array, O(1)
not indexed like an array, can't random access, O(n)
'''