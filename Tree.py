import argparse
import AVL
import BST

BSTtestTree = BST.binary_search_tree()
AVLtestTree = AVL.AVLTree()

def readFile(fileName):
    countA = 0
    countB = 0

    try:
        fileObject = open(fileName, "r")

        for line in fileObject:
            line = line.lower()
            countA = BSTtestTree.insert(line)
            countB = AVLtestTree.insert(line)

        print("THIS IS BST")
        BSTtestTree.height()
        print("Total Duplicates: ", BSTtestTree._getDups())

        print("Total Inserted: ", countA)

        print("THIS IS AVL")
        print("Height of AVL tree is: " , AVLtestTree.height())
        print("Total Duplicates: ", AVLtestTree._getDups())

        print("Total Inserted: ", countB)

    except IOError:
        print("Error opening file")

def delVal(fileName2):
     try:
         fileObject = open(fileName2, "r")

         for line in fileObject:
             line = line.lower()
             AVLtestTree.delete_value(line)

         print("Deletes: ", AVLtestTree._getDel())
     except IOError:
         print("Error opening file")

# get input
def main():
    running = True
    while running:
        try:
            parser = argparse.ArgumentParser()
            parser.add_argument('exp', help = "Enter expression")
            parser.add_argument('exp2', help="Enter expression")
            fileName = parser.parse_args()
            fileName2= parser.parse_args()
        except SystemExit:
            print("No input found")
        else:
            readFile(fileName.exp)
            delVal(fileName2.exp2)
        running = False




main()
