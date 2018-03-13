#Name: Russell Sammut-Bonnici
#ID: 0426299(M)
#Task: 4

#class concerned with initialising node
class Node:

    #initializes node
    def __init__(self, value=None):
        self.value = value
        self.leftChild = None
        self.rightChild = None


#class concerned with Binary Search Tree functions
class BinarySearchTree:

    #initializes tree
    def __init__(self):
        self.root = None

    #inserts node into the tree, calls _insertNode after root is set
    def insertNode(self, value):

        if self.root == None:
            self.root = Node(value)
        else:
            self._insertNode(value, self.root)

    #recursive function called for inserting node after root
    def _insertNode(self, value, currNode):

        #when the value is less than its previous
        if value < currNode.value:

            #if left child doesn't exist add as left, else add under left
            if currNode.leftChild == None:
                currNode.leftChild = Node(value)
            else:
                self._insertNode(value, currNode.leftChild)

        #when the value is more than its previous
        elif value > currNode.value:

            #if right child doesn't exist add as right, else add under right
            if currNode.rightChild == None:
                currNode.rightChild = Node(value)
            else:
                self._insertNode(value, currNode.rightChild)

        #when the value is equal to its previous
        else:
            print "Error: Inserted value is already in the Binary Search Tree."
            return -1

    #prints the tree with all its contained nodes
    def printTree(self):

        #prints tree when root is not null with recursive function call
        if self.root!=None:
            self._printTree(self.root)
        else:
            print("Error: Tree does not have any nodes to print out")
            return -1

    #recursive function called for printing nodes left to right
    def _printTree(self,currNode):

        #base case is when the bottom of the tree is reached (when node==None)
        if currNode!=None:
            self._printTree(currNode.leftChild)
            print str(currNode.value)
            self._printTree(currNode.rightChild)



bst = BinarySearchTree() #initializing instance of class

#incrementally building up bst with a sequence of integers
bst.insertNode(8)
bst.insertNode(6)
bst.insertNode(9)
bst.insertNode(1)
bst.insertNode(3)
bst.insertNode(2)
bst.insertNode(4)
bst.insertNode(5)
bst.insertNode(10)

print("The Binary Search Tree's nodes from left to right are:")
bst.printTree()
