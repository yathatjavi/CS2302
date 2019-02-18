#Provied by Olac Fuentes
#for CS2302
#edited and completed by yathatjavi
#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()     

def Prepend(L,x):
    if L.head == None:
        L.head = Node(x)
        L.tail = L.head
    else:
        temp = Node(x)
        temp.next = L.head
        L.head = temp

def GetLengthRec(L):
    
    if L.head == None:
        return 0
    if L.head.next == None:
        return 1
    else: 
        L.head = L.head.next
        return 1+GetLength(L)
def GetLength(L):
    temp = L.head
    size =0
    while temp != None:
        size+=1
        temp = temp.next
    return size

def InsertAfter(L, W,x):
    tempNode = Node(x)
    if L.head.item == W:
        tempNode.next = L.head.next
        L.head.next = tempNode
    temp = L.head
    while temp.next != None and temp.next != W:
        temp = temp.next
    if temp.next != None:
        tempNode.next = temp.next.next
        temp.next.next = tempNode
        if tempNode.next == None:
            L.tail = tempNode
        
    

L = List()
#print(IsEmpty(L))
for i in range(5):
    Append(L,i)

Print(L)   
#Prepend(L,12)
#print(GetLength(L))
InsertAfter(L,2,15)
Print(L)
'''
Print(L)
PrintRec(L)
PrintReverse(L)

Remove(L,2)
Print(L)
Remove(L,20)
Print(L)
Remove(L,0)
Print(L)
Remove(L,4)
Print(L)
print(L.head.item)
print(L.tail.item)
'''