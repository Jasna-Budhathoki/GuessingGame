class TreeNode:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

    def getData(self):
        return self.data

    def setData(self, newValue):
        self.data = newValue

    def getLeftChild(self):
        return self.leftChild

    def setLeftChild(self, node):
        self.leftChild = node

    def getRightChild(self):
        return self.rightChild

    def setRightChild(self, node):
        self.rightChild = node

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild() == None

    def __str__(self):
        return str(self.data)
