class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.tamnho=0
class Linkedlist:
    def __init__(self):
        self.head=None
    
    def __append__(self,valor):
        novo =Node(valor)

        if self.head==None:
            self.head=novo
        
        atual=self.head

        while atual.next is not None:
            atual=atual.next
        
        atual.next=novo# o atual assume papel de ponteiro
        self.tamnho+=1
    
    def __print__(self):

        atual=self.head
        while atual is not None:
            print(atual.data)
            atual=atual.next
        
    def __len__(self):
        return self.tamnho
    
    def __getitem__(self,index):
        atual=self.head
        for i in range(index):
            if atual is not None:
                atual=atual.next
            else:
                raise IndexError("Error")                
        if atual is not None:
            return atual.data
        else:
            raise IndexError("Error")
        
    def __set__(self,index,elem):
        atual=self.head
        for i in range(index):
            if atual is not None:
                atual=atual.next
            else:
                raise IndexError("Error")
        if atual is not None:
            atual.data=elem
        else:
            raise IndexError("Error")
    
    def index(self,elem):
        i=0
        atual=self.head
        while(atual is not None):
            
            if atual.data==elem:
                return i
            atual=atual.next
            i+=1
        raise ValueError(f"{elem} is not list")
    def invert(self):
        atual=self.head
        anterior=None
        

        while atual is not None:
            proximo=atual.next
            atual.next=anterior
            anterior=atual
            atual=proximo
        self.head=anterior
        
    def insert(self, indec, elem):
      node = Node(elem)  

      if indec == 0:
        node.next = self.head
        self.head = node
      else:
        atual = self.head
        for c in range(indec - 1):
            if atual is not None:
                atual = atual.next
            else:
                raise IndexError("Erro de index")

        if atual is None:
            raise IndexError("Erro de index")

        node.next = atual.next
        atual.next = node

    def remove(self,elem):
        if self.head == None:
            return IndexError("Error")
        if self.head.data==elem:
            self.head=self.head.next
            self.tamnho=self.tamnho-1
        else:
            anterior=self.head
            atual=self.head
            while atual is not None:
                if atual.data==elem:
                    anterior.next=atual.next
                    atual.next=None
                    self.tamnho-=1
                    return
                else:
                    atual=atual.next
                    anterior=anterior.next

