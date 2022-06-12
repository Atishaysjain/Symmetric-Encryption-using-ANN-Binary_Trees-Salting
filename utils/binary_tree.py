import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # This will not print tensorflow warnings


inorder = []
preorder = []


class Node:
    def __init__(self, key, left = None, right = None):
        self.data = key
        self.left = left
        self.right = right



# Creates a binary tree using level order traversal, 2 nodes per branch
def makeTree(s): 
    
    root=Node(s[0])
    queue = []
 
    queue.append((root,0))
 
    while(len(queue) > 0):
        sz=len(queue)
        for i in range(0,sz):
            node,index = queue.pop(0)
    
            if (index*2+1) < len(s):
                node.left=Node(s[index*2+1])
                queue.append((node.left,index*2+1))
    
            if (index*2+2) < len(s):
                node.right=Node(s[index*2+2])
                queue.append((node.right,index*2+2))
    
    return root



# Returns the level order traversal of the tree
def getLevelOrder(root):
    
    if root is None:
        return

    queue = []
 
    queue.append(root)

    levelorder = []
    
    while(len(queue) > 0):
        
        sz=len(queue)
        
        for i in range(0,sz):
            
            levelorder.append(queue[0].data)
            node = queue.pop(0)
    
            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        
    return levelorder


# Returns the preorder traversal of the tree
def getPreorder(root):
    
    preorder.append(root.data)
    
    if root.left is not None:
        getPreorder(root.left)
    
    if root.right is not None:
        getPreorder(root.right)


# Returns the inorder traversal of the tree
def getInorder(root):
    
    if root.left is not None:
        getInorder(root.left)
    
    inorder.append(root.data)
    
    if root.right is not None:
        getInorder(root.right)


# Recursive function to construct a binary tree from a given inorder and preorder sequence
def construct(start, end, preorder, pIndex, d):
 
    if start > end:
        return None, pIndex
 
    root = Node(preorder[pIndex])
    pIndex = pIndex + 1
 
    index = d[root.data]
 
    root.left, pIndex = construct(start, index - 1, preorder, pIndex, d)
 
    root.right, pIndex = construct(index + 1, end, preorder, pIndex, d)
 
    return root, pIndex



# Construct a binary tree from inorder and preorder traversals.
def constructTree(inorder, preorder):
 
    d = {}
    for i, e in enumerate(inorder):
        d[e] = i

    pIndex = 0
 
    return construct(0, len(inorder) - 1, preorder, pIndex, d)[0]



# modifies duplicates so that a binary tree could be constructed using preorder and inorder traversal. 
# Eg. ['a', 'a', 'b', a', 'b'] would become ['a', 'a*', 'b', a**', 'b*']

def modify_duplicates(input_list):
    
    for index, i in enumerate(input_list):
        
        if i in input_list[index+1:]:
            num = 1
        
            for j in range(index+1, len(input_list)):
                
                if(input_list[j] == i):
                    append_str = '*'*num
                    input_list[j] = f'{i}{append_str}'
                    num += 1
                    
    return input_list



# This function removes "*" from the output list as "*" were added to make sure that each element is a unique element 

def remove_stars(input_list):
    
    for i in range(0, len(input_list)):
        if '*' in input_list[i]:
            input_list[i] = input_list[i].split('*')[0]
            
    return input_list



def encrypt_binary_tree(lvl1):
    
    s = modify_duplicates(input_list = lvl1)
    
    root = makeTree(lvl1)
        
    getInorder(root)
    
    getPreorder(root)
    
    return inorder, preorder



def decrypt_binary_tree(inorder, preorder):
    
    root2 = constructTree(inorder, preorder)
    
    levelorder = getLevelOrder(root2)
    
    lvl1 = remove_stars(input_list = levelorder)
    
    return lvl1