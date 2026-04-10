class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
class Solution:
    def buildTree(Node,n,arr):
        if n==0:
            return None
        q=[]
        for i in range(n):
            q.append(Node)