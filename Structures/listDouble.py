class Node:

    def __init__(self, id):  # constructor of class Node
        self.id = id  # assign the value 
        self.next = None  # assign the next pointer 
        self.previous = None  # assign the previous pointer 


class DoublyLinkedList:
    def __init__(self):  
        self.head = None  

    # add method
    def add(self, node):
        if self.head is None:  
            self.head = node  
        else:
            temp = self.head
            while temp.next is not None:  
                temp = temp.next  
            temp.next = node  
            node.previous = temp  

    # print method
    def print_list(self, direction):
        if self.head is None:  
            print('The list is empty')  
        else:
            if direction is 'forward': 
                temp = self.head
                while temp.next is not None:  # iterate thru the list to print each element
                    print(temp.id, end='')  # print each element
                    print('->', end='')
                    temp = temp.next
                print(temp.id)
            elif direction is 'backward':  # check for direction sent as a parameter
                temp = self.head
                while temp.next is not None:  # get to the last element of the list
                    temp = temp.next
                while temp.previous is not None:  # iterate backwards thru the list to print each element
                    print(temp.id, end='')  # print each element
                    print('->', end='')
                    temp = temp.previous
                print(temp.id)
            else:
                print('Error, wrong direction to print list specified')


cadena = input(" Introduce una cadena de texto: ")
print("La cadena que ingreso es: ", cadena, end='\n')
list2 = DoublyLinkedList()  # create a new list

for i in [1, 2, 3]:
    if cadena == '*':
        a = '*'
        print("*")
        list2.add(Node(a))
    else:
        b = '+'
        print('+')
        list2.add(Node(b))


# in this part view the list
list2.print_list('forward')  # print the list forward
list2.print_list('backward')  # print the list backwar

cadena1 = input(" presione una tecla para salir: ")