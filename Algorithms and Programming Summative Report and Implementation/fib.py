def recFib(n):
    if n == 1 or n ==2:
        return  1
    else:
        return(recFib(n-1) + recFib(n-2))
def itFib(n):
    n1 = 1
    n2 = 1
    while n>2:
        n1, n2 = n2, n1 + n2
        n-=1
    return n2
def InsertionSort(a):
    for i in range(1,len(a)):
        current = a[i]
        j = i-1
        while j >= 0 and a[j] > current:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = current

def MaxHeapify(A,i,size):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    for c in [l,r]:
        if c < size and A[c] > A[largest]:
            largest = c
    if largest == i:
        return
    swap(A,i,largest)
    MaxHeapify(A, largest, size)
    
def BuildMaxHeap(A):
    i = len(A)//2 - 1
    size = len(A)
    while i >= 0:
        MaxHeapify(A,i,size)
        i -= 1

def HeapSort(A):
    BuildMaxHeap(A)
    size = len(A)
    while size > 1:
        swap(A,0, size-1)
        size -= 1
        MaxHeapify(A,0,size)


def CountingSort(A,B,k):
    C = [0 for i in range(0,k+1)]
    for j in range(0,len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1

def BucketSort(A):
    n = len(A)
    B = [[] for i in range(0,n)]
    C = []
    for i in range(0,n):
        k = int(n*A[i]//1)
        B[k].append(A[i])
    for i in range(0,n):
        InsertionSort(B[i])
        C += B[i]
    return C

def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1
def Quicksort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
class Node:
    def __init__ (self, item,next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item,self.head)
        self.head = temp
    def addAtEnd(self,v):
        node = Node(v,None)
        if self.tail == None and self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self,v):
        node = Node(v,self.head)
        self.head = node
    def pop(self):
        node = self.head
        self.head = self.head.next
        return node.item
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self. n = 0
    def __len__(self):
        return self.n
    def enqueue(self,v):
        if self.tail==None and self.head == None:
            node = Node(v,None)
            self.head = node
            self.tail = node
        else:
            node = Node(v,None)
            self.tail.next = node
            self.tail = node
        self.n += 1
    def dequeue(self):
        node = self.head
        self.head = self.head.next
        self.n -= 1
        return node.item

class HashTable():

    def __init__(self,m):
        self.keys = [LinkedList() for i in range(0,m)]
        self.m = m
    def insert(self,key):
        i = hash(key) % self.m
        self.keys[i].add(key)
    def delete(self,key):
        i = hash(key) % self.m
        self.keys[i].remove(key)
    def search(self,key):
        i = hash(key) % self.m
        return self.keys[i].search(key)





                 


























