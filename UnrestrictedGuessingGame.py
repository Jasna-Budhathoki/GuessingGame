from BinaryTree import BinaryTree
from TreeNode import TreeNode
from GameTreeReader import GameTreeReader
from GuessingGame import GuessingGame
import sys

class UnrestrictedGuessingGame(GuessingGame):
    """Inherits methods from parent class GuessingGame. If the user was thinking of a country that is not pre-existing, UnrestrictedGuessingGame adds a new country to the tree."""
    def __init__(self,tree):
        super().__init__(tree)

    def playGame(self,node):
        """Overriding playGame method which calls game method from GuessingGame if the user is ready to begin."""
        self.printLeaf(self.tree.root)
        gameyes0 = input("Choose any country, on or off list, and I will try to guess it. Are you ready to begin?")
        if gameyes0 == "yes":
            print("Okay.Let's begin. Please answer yes/no question by typing 'yes' or 'no' ")
            self.game(self.tree.root)

    def wrongGuess(self,userinput,node):
        """Overriding wrongGuess method which adds a new node if the user was thinking of a non pre-existing country"""
        if userinput == "yes":
            print("Yay! I guessed it!")
        elif userinput == "no":
            newCountry = input("Which country were you thinking of? ")
            newQuestion = input("Please give me a yes/no question that would have determined your country ")
            yesNo = input("Is your answer to the question yes or no? ")
            oldCountry = TreeNode(node.getData()) #stores the leaf node to oldCountry
            newCountry = TreeNode(newCountry) #creates a new node called newCountry
            node.setData(newQuestion) #sets the node to newQuestion
            if yesNo == "yes":
                node.setLeftChild(newCountry) #sets left child to newCountry
                node.setRightChild(oldCountry) #sets right child to oldCountry
            elif yesNo == "no":
                node.setRightChild(newCountry)
                node.setLeftChild(oldCountry)
        play1 = input("Would you like to play again?[yes/no]: ")
        if play1 == "yes":
            self.playGame(self.tree.root)
        if play1 == "no":
            print("Okay.Bye")

def main():
    newTree = GameTreeReader(sys.argv[1]).getTree()
    Tree = UnrestrictedGuessingGame(newTree)

if __name__ == '__main__':
    main()
