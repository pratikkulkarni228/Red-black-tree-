"""
@author : Pratik kulkarni
Red black tree with following features:
-Insertion
-Inorder traversal and printing
-Depth/Height of a tree
-Search and return height of a particular node
-Leftrotate
-Rightrotate
-Invertcolor
"""
#################################################
from random import *

"""INPUT SEQUENCE 1"""
input1 = list()
for i in range (500):
    input1.append(randint(1, 100))


"""INPUT SEQUENCE 2"""
input2 = list()
for i in range(1,100):
    if i%2!=0:
        input2.append(i)
for i in range(1,100):
    if i%2==0:
        input2.append(i)
for i in range(401):
    input2.append(randrange(1,100))

black = "black"
red = "red"


class RBTnode:

    def __init__(self, keyval):
        self.keyval = keyval
        self.left = None
        self.right = None
        self.color = red
        
        """This  variable is used to store the count of the
        repeating elements(keys) in the input without re-adding the key"""
        self.count =1

def redorblack(node):
    return colornode(node) == red

def colornode(node):
    if not node:
        return black
    return node.color

def leftrotate(head):           #Rotate left
    node = head.right
    head.right = node.left
    node.left = head
    node.color = head.color
    head.color = red
    return node

def rightrotate(head):          #Rotate right
    node = head.left
    head.left = node.right
    node.right = head
    node.color = head.color
    head.color = red
    return node

def invertcolor(node):          #Invert the color after rotation
    node.left.color = black
    node.right.color = black
    node.color = red
    return node

def insert(node, keyval):
    if not node:
        return RBTnode(keyval)
    if keyval==node.keyval:             
        node.count +=1                              #Increment the count if the same element is found
    elif keyval > node.keyval:
        node.right = insert(node.right, keyval)        #call right tree recursively
    else:
        node.left = insert(node.left, keyval)           #call left tree recursively

    if redorblack(node.right) and not redorblack(node.left):    
        node = leftrotate(node)                                 
    if redorblack(node.left) and redorblack(node.left.left):
        node = rightrotate(node)
    if redorblack(node.left) and redorblack(node.right):
        node = invertcolor(node)
    return node


def inorder(node):
    if node != None:
        inorder(node.left)
        print node.keyval
        #print node.color
        inorder(node.right)

def depth(node):
    if node==None:
        return 0
    else:
        leftD = depth(node.left)
        rightD = depth(node.right)
        if (leftD > rightD):
            return leftD+1
        else:
            return rightD+1

"""Search for a key"""

"""returns: The height of that element multiplied by the count"""

def search(node,keyval,counter):

    if node==None:                 #check if root exists node exists
        return 0
    else:
        counter = counter+1         #COUNTER DENOTES HEIGHT OF THAT ROOT
        if keyval == node.keyval:
            global freq             #DENOTES NO OF TIMES THE ELEMENT WAS INSERTED
            freq = node.count
            return counter * freq
        elif keyval<node.keyval:
            return search(node.left,keyval,counter)
        elif keyval>node.keyval:
            return search(node.right,keyval,counter)


###################################################

tree =None
avg=0.0
testarr = [10,10,20,20,1,15,17,40,50,60]

print "---A Red Black Tree----"

for i in input1:
    tree = insert(tree,i)

print "Elements Inserted for: INPUT SEQUENCE 1"

for i in range(1,100):
    a = search(tree,i,0)
    avg=avg+a
avg=avg/500
print "Average key comparisons:" , avg


#################################################
#Uncomment this to print the elements inorder
#inorder(tree)
##################################################

print "Height of the tree is :", depth(tree)
