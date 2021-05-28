# Huffman Decoding

import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq # 빈도
        self.data = data # 값
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():#builds the tree and returns root
    q = Queue.PriorityQueue()
   
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key))) # freq, key, node
    
    while q.qsize() != 1: # 값이 있다면
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' ) #빈도+빈도
        obj.left = a[2] # 노드
        obj.right = b[2] # 노드
        q.put((obj.freq, obj.data, obj ))
        
    root = q.get()
    root = root[2] #contains root object 노드 반환
    return root

def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")
    dfs_hidden(obj.left, already + "0")

def decodeHuff(root, string):
    ans=''
    current=root

    for s in string:
        if s=='1':
            current=current.right
        else:
            current=current.left

        if not (current.left and current.right):
            ans+=current.data
            current=root

    print(ans)

if __name__=="__main__":
    ip = input()
    freq = {}#maps each character to its frequency

    cntr = 0

    for ch in ip:
        if(freq.get(ch) == None): # dict    
            freq[ch]=1
        else:
            freq[ch]+=1

    root=huffman_hidden() #contains root of huffman tree

    code_hidden = {}#contains code for each object

    dfs_hidden(root, "")

    if len(code_hidden) == 1:#if there is only one character in the i/p
        for key in code_hidden:
            code_hidden[key] = "0"

    toBeDecoded = ""

    for ch in ip:
        toBeDecoded += code_hidden[ch]

    decodeHuff(root, toBeDecoded)
