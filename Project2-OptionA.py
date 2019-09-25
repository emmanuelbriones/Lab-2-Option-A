class Node(object):
    item = -1
    next = None


    def __init__(self, item, next):
        self.item = item
        self.next = next
    
    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def setItem(self, new_data):
        self.item = new_data

    def setNext(self, new_next):
        self.next = new_next


class Linked_List(object):
    item = -1
    head = None

    def _init_(self, head):
        self.head = head
    
    def add_head(self, item):
        self.head = Node(item, self.head)

    def solution1(self):
        # set head as temporary node
        temporary = self.head
        # traverse all the list except for the last one
        while temporary.getNext() != None:
            # current node equals the data inside temporary node
            current = temporary.getItem()
            # temporary2 equals the current's next node
            temporary2 = temporary.getNext()
            # traverses all the nodes after the current node being compared
            while temporary2 != None:
                # compare the current data to the rest of the data of the nodes of the linked list
                if current == temporary2.getItem():
                    print("ID Duplicates: " + str(current))
                # move to the next node to compare with the current node
                temporary2 = temporary2.getNext()
            # move to the next node to compare it with the rest of the node of the list
            temporary = temporary.getNext()

    def bubble_sort(self):
        # set a variable to none
        end_of_list = None
        # keep iterating until the end of the list is equal to the head of the list
        while end_of_list != self.head:
            # set the head as the previous node that will be compared to the next one
            previous = self.head
            # iterate until you reach the end of the list
            while previous.getNext() != end_of_list:
                # assign the next node to a variable
                next_node = previous.getNext()
                # compare to see which data is bigger and swap
                if previous.getItem() > next_node.getItem():
                    previous.item, next_node.item = next_node.getItem(), previous.getItem()
                # move to the next node
                previous = previous.getNext()
            # assign the last node as your new end of list
            end_of_list = previous

    def find_duplicates(self):
        # assign a head
        head = self.head
        # iterate until reaching the last node
        while head.getNext() != None:
            # compare the current node with the next node to find duplicates
            if head.getItem() == head.getNext().getItem():
                print(head.getItem())
            # move to the next node and repeat the process
            head = head.getNext()
            
    def split_Lists(self):
        slow_Node = self.head
        fast_Node = self.head
        while fast_Node != None:
            fast_Node = fast_Node.next.next
            slow_Node = slow_Node.next
        middle_Node = slow_Node
        slow_Node.next = None
        return head, middle_Node

    def merge_Sort(self):
        head = self.head
        if head == None or head.next == None:
            return head
        first_half_of_list, second_half_of_list = self.split_Lists()
        first_half_of_list = self.merge_Sort(first_half_of_list)
        second_half_of_list = self.merge_Sort(second_half_of_list)
        head = self.merge_Lists(first_half_of_list, second_half_of_list)
        return head


    def merge_Lists(self, first_half_of_list, second_half_of_list):
        temporary_Node = None
        if first_half_of_list == None: return second_half_of_list
        elif second_half_of_list == None: return first_half_of_list
        if second_half_of_list.item > first_half_of_list.item:
            temporary_Node = first_half_of_list
            temporary_Node.next = self.merge_Lists(first_half_of_list.getNext(), second_half_of_list) 
        else:
            temporary_Node = second_half_of_list
            temporary_Node.next = self.merge_Lists(first_half_of_list,second_half_of_list.getNext())
        return temporary_Node


def getHighestValue(list1):
    highestValue = list1[0]
    # traverse all the way to the second to last element
    for i in range(len(list1-1)):
        # compare with every element to find the highest value
        if highestValue < list1[i+1]: highestValue = list1[i+1]
    return highestValue

def solution4(list1, list2):
    # find highest value for first list
    highestValue1 = getHighestValue(list1)
    # find highest value for second list
    highestValue2 = getHighestValue(list2)
    #compare two highest values and create an arraylist with the biggest value
    if highestValue1 > highestValue2:
        newlist = []
        # create an array of size highestvalue1 and initialize all values to false
        for i in range (highestValue1):
            newlist[i] = False
        # find the value of the element and put it on the new list and convert to true
        for i in range (len(list1)):
            if list1[i] == newlist[list1[i]]:
                newlist[list1[i]] = True
        # if it is true, then it was already visited and you print the duplicate
        for i in range(len(list2)):
            if list2[i] == newlist[list2[i]] and newlist[list2[i]] == True:
                print("Duplicate ID: " + str(list2[i]))
    else:
        newlist = []
        # create an array of size highestvalue2 and initialize all values to false
        for i in range (highestValue2):
            newlist[i] = False
        # find the value of the element and put it on the new list and convert to true
        for i in range (len(list1)):
            if list1[i] == newlist[list1[i]]:
                newlist[list1[i]] = True
        # if it is true, then it was already visited and you print the duplicate
        for i in range(len(list2)):
            if list2[i] == newlist[list2[i]] and newlist[list2[i]] == True:
                print("Duplicate ID: " + str(list2[i]))

def main():
    # open the activision file to be read
    Act = open("activision.txt", "r")
    # read the file line by line and assign it to a list
    Act2 = Act.readlines()
    # create a linked list
    LL = Linked_List()
    # traverse the list with all the ID's and add head to linked list
    for i in range(len(Act2)):
        LL.add_head(Act2[i])
    print(len(Act2))
    print(LL.head.item)
    temp = LL.head
    counter = 0
    while temp != None:
        counter+=1
        temp = temp.getNext()
    print(counter)
    # open the vivendi file to be read
    Viv = open("vivendi.txt","r")
    # create another list containing the values of each line of vivendri
    Viv2 = Viv.readlines()
    # traverse the list of the second file to keep on adding to the linked list to have all 6000 ids
    for i in range (len(Viv2)):
        LL.add_head(Viv2[i])
    current = LL.head
    counter=0
    while current != None:
        counter+=1
        current = current.getNext()
    print(counter)
    print(len(Viv2))
    print(LL.head.item)
    #integer = LL.head.getItem()
    #current2 = LL.head
    LL.solution1()
    LL.bubble_sort()
    print(LL.head.item)
    current2 = LL.head
    current3 = LL.head
    counter=0
    while current3 != None:
        counter+=1
        current3 = current3.getNext()
    print(counter)
    #while current2 != None:
        #print(current2.getItem())
        #current2 = current2.getNext()

    LL2 = Linked_List()
    LL2.add_head(5)
    LL2.add_head(2)
    LL2.add_head(34)
    LL2.add_head(-32)
    LL2.add_head(20)
    LL2.bubble_Sort()
    current2 = LL2.head
    while current2 != None:
        print(current2.getItem())
        current2 = current2.getNext()
    solution4(Act2, Viv2)



main()