class Node:
    def __init__(self, id):     
        self.id = id            
        self.next = None       

class CircularLinkedList:
    def __init__(self):         
        self.head = None        

    # method add
    def add(self,node):
        if self.head is None:   
            self.head = node    
            self.head.next = node    
        else:
            temp = self.head
            while temp.next is not self.head:  
                temp = temp.next                 
            temp.next = node                     
            node.next = self.head                

    #print method
    def print_list(self):
        if self.head is None:               
            print('The list is empty')      
        else:
            temp = self.head
            while temp.next is not self.head:    
                print(temp.id,end='')            
                print('->',end='')
                temp = temp.next
            print(temp.id,end='')                
            print('->',end='')
            temp = temp.next
            print(temp.id)
#created the other list 
list = CircularLinkedList()     
#insert the name 
cadena = input(" Introduce una cadena de texto: ")
print("La cadena que ingreso es: ", cadena, end='\n')
#add to the list 
list.add(Node(cadena))       


list.print_list()       #print the list
#pause
cadena1 = input("Presione enter para salir")