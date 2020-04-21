'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

How do you find and return the middle node of a singly linked list in one pass?
You do not have access to the length of the list.
If the list is even, you should return the first of the two "middle" nodes.
You may not store the nodes in another data structure.

store count

Team Members
Miguel, Russ, Eric

Problem Description
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

How do you find and return the middle node of a singly linked list in one pass?
You do not have access to the length of the list.
If the list is even, you should return the first of the two "middle" nodes.
You may not store the nodes in another data structure.

Understand
What is the problem asking you to do?
Find the middle node in a singly linked list only looping once

What format do you need to deliver the solution in?


Plan
How will you solve this problem?


What is your pseudocode?


Execute
Paste your code here:


Reflect
What is the time complexity of your solution?  How did you derive this?


What elements of your solution can be improved?

'''

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def add(self, value):
#         self.next = Node(value)

# singly_linked_list = Node(1)
# singly_linked_list.add(2)

# # def find_middle(list):
# print(singly_linked_list.__dict__)
# print(singly_linked_list.next.__dict__)

# ***************************************************************************************************

'''
How do you reverse a singly linked list without recursion?
You may not store the list, or it's values, in another data structure.

for each item in list:
change first value link to None
take the first value pointer save to temp variable
iterate to next value
trade links with temp variable and next value pointer
iterate until pointer is None (this is the end of list and the last iteration) this will be the new head
this should be one pass
'''