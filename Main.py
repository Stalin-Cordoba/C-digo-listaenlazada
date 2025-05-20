import os
from LinkedList import LinkedList
from LinkedList import Node

def main():
    myList=LinkedList()
    n1=Node(3)
    n2=Node(3) 
    n3=Node(2)
    n4=Node(8)
    n5=Node(10)
    n6=Node(10)
    n7=Node(16)
    myList.insertNode(n1)
    myList.insertNode(n2)
    myList.insertNode(n3)
    myList.insertNode(n4)
    myList.insertNode(n5)
    myList.insertNode(n6)
    myList.insertNode(n7)
    os.system("cls") 
    print(f"Nodo eliminado + {myList.delete(2)}")
    print(f"Nodo eliminado + {myList.delete(10)}")
    myList.printList()

main()
    