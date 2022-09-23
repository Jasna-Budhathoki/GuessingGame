#Jasna Budhathoki
#CS 205-02-PY
#Assignment 6

from BinaryTree import BinaryTree
from TreeNode import TreeNode
from GameTreeReader import GameTreeReader
import sys

class GuessingGame():
    """The choice of things is pre-specified. The user picks a thing and the program guesses the answer by asking user yes/no questions"""
    def __init__(self,tree):
        self.tree = tree
        self.promptUser(self.tree.root)

    def printLeaf(self,node):
        """Prints the leaves of the tree"""
        if node.isLeaf() == True: #checks if the node is a leaf
            print(node)
        else:
            self.printLeaf(node.getLeftChild())
            self.printLeaf(node.getRightChild())

    def promptUser(self,node):
        """Asks user if they want to play a guessing game"""
        play0 = input("Do you want to play a guessing game?[yes/no]: ")
        if play0 == "yes":
            print("Okay! Here are the names of countries:")
            self.playGame(node) #Calls playGame method
        elif play0 == "no":
            print("Okay.Bye")

    def playGame(self,node):
        """Calls printLeaf method to show pre-specified countries and then calls game method if the user is ready to begin."""
        self.printLeaf(self.tree.root) #calls printLeaf method
        gameYes = input("Choose one and I will try to guess it. Are you ready to begin? [yes/no]: ")
        if gameYes == "yes":
            self.game(self.tree.root)

    def game(self,node):
        """If user says yes, goes to the left child, if the user says no, goes to the right child until it reaches a leaf."""
        if node.isLeaf() == True: 
            input1 = input("Were you thinking of" + " " + str(node) + "?" + ":" + " ")
            return self.wrongGuess(input1,node) #calls wrongGuess method with input1 and node as parameters
        else:
            game2 = input(node)
            if game2 == "yes":
                return self.game(node.getLeftChild())

            elif game2 == "no":
                return self.game(node.getRightChild())

    def wrongGuess(self,userinput,node):
        """prints a comment based on the final input from game method. Then asks user if they want to play again."""
        if userinput == "yes":
            print("Yay! I guessed it!")
        elif userinput == "no":
            print("Oh, I guessed it wrong?")
        play1 = input("Would you like to play again?[yes/no]: ")
        if play1 == "yes":
            self.playGame(self.tree.root) #calls playGame method if the user wants to play again
        if play1 == "no":
            print("Okay.Bye")

def main():
    newTree = GameTreeReader(sys.argv[1]).getTree()
    Tree = GuessingGame(newTree) #creates a tree object

if __name__ == '__main__':
    main()
