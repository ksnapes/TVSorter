'''

Created on Mar 10, 2015
@author: Snapes

'''
import os

endSession = False
 

def displayOptions(currentDir):
    for file in os.listdir(path=currentDir):
        print(file)
     
def sortFiles(currentDir):
    
    tagMatch = []
    tag = input("Enter tag to sort by: ")
    sortToFolder = input("Sort to folder: ")
    sortByTags = tag.split()
    
    for file in os.listdir(path=currentDir):
        if (file != sortToFolder):
                
            termCount = 0
            for term in sortByTags:
    
                if term in file.lower():
                    termCount = termCount + 1
    
            if(termCount == len(sortByTags)):
                print(file + "\n")
                tagMatch.append(file)
                
    confirm = input("Do you want to move these files? [Y/N]: ")
        
    if (confirm.lower() == "n"):
        print("Move cancelled")
        return
    elif (confirm.lower() == "y"):
        print("Moving...")
                
    if not os.path.exists(currentDir + sortToFolder):
        os.makedirs(currentDir + sortToFolder)
        
    for file in tagMatch:
        os.rename(currentDir + file, currentDir + sortToFolder + "\\" + file)
            

    if(confirm.lower() == "y"):
        print("Move complete.")


currentDir = input("Enter directory to be sorted: ")
if not currentDir.endswith("\\"):
    currentDir = currentDir + "\\"
    
while(endSession == False):
    print("\n1. Display files")
    print("2. Sort files")
    print("3. Change directory")
    print("4. Quit \n")
    userChoice = input("Type number to select option: ")
    if(userChoice == "1"):
        displayOptions(currentDir)
    elif(userChoice == "2"):
        sortFiles(currentDir)
    elif(userChoice == "3"):
        currentDir = input("Enter new directory: ")
    elif(userChoice == "4"):
        endSession = True
    
    
