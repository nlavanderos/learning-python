#https://leetcode.com/problems/add-two-numbers/
#leetCode Challenge -02 

class Node:
    """
    Creacion de nodo\n
    Por ejemplo un entero:
    >>> Node(1)
    """

    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    """
    Creacion de Single Linked List \n
    Uso:
    >>> Linked()
    """
    
    def __init__(self):
        self.head=None
        self.size=0

    def agrega(self,value):
        miNodo=Node(value)

        if (self.size==0 or self.head==None):
            self.head=miNodo
        
        else:
            current=self.head

            while(current.next!=None):

                current=current.next

            current.next=miNodo

        self.size+=1


    
    def elimina(self,value):
    
        if (self.size==0):
            print(f'No se puede eliminar {value} , la linked list esta vacia')
            return 0
        else:
            recorre=self.head
            if(recorre.data==value):
                    self.head=None
                    self.size-=1
                    return 0
            try:
                
                while(recorre.next.data!=value):
                    recorre=recorre.next
                encontrado=recorre.next
                recorre.next=encontrado.next
            except AttributeError:
                return print(f'No se encontro {value}')
            
            
        self.size-=1


    def imprime(self):
        printValue=self.head
        if(printValue==None):
            print(printValue)
        while(printValue is not None):
            print(printValue.data)
            printValue=printValue.next

    def __str__(self) -> str:
        string='['
        current=self.head
        for i in range(len(self)):
            string+=str(current.data)
            if i!=len(self)-1:
                string+=str(', ')
            current=current.next
        string+=']'
        return string
        
    def __len__(self) -> int:
        return self.size


listado=Linked()
listado.agrega('Lunes')
listado.elimina('Lunes')
listado.agrega('Martes')
listado.imprime()
print(listado.__len__())
print(listado)

