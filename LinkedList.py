class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next
    
    def insertNode(self, node):
        if self.head == None:
            self.head = node
        else:
            if node.key <= self.head.key:
                node.next = self.head
                self.head = node
            else:
                current = self.head
                while current.next is not None and current.next.key <= node.key:
                    current = current.next
                node.next = current.next
                current.next = node
                
    def delete(self,key):
        firstFlag = False
        while self.head and self.head.key==key:
            if(self.head.next):
                self.head=self.head.next 
                firstFlag = True   
            else:
                self.head=None
        else:
            if  firstFlag:
                 return key
            current=self.head
            flag = False
            while current and current.next:
                if current.next.key == key:
                    current.next = current.next.next
                    flag = True
                elif current.next.key > key:
                    if flag:
                        return key
                    else:
                        return None
                else:
                    current = current.next
                    

class Node:
    def __init__(self, dato):
        self.key = dato
        self.next = None
        
    def __str__(self):
        return f" Clave  -> {self.key}"