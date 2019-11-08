##Fehler
class Node:
    def __init__(self,info): 
        self.info = info  
        self.left = None  
        self.right = None 

def sort(v1, v2):
    if v1 > v2:
        return v2, v1
    return v1, v2

def lca(root, v1, v2):
    #Enter your code here
    v1, v2 = sort(v1, v2)
    while True:
        if root.info >= v1 and root.info <= v2:
            return root
        if root.info < v1:
            root = root.right
        elif root.info > v2:
            root = root.left