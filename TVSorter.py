'''
Created on Mar 10, 2015

@author: Snapes
'''
import os

endSession = False

while (endSession == False):
      
    currentDir = "C:\\Users\\Kieran\\Files\\Torrents\\Bobs Burgers" 
    itemList = []
    fileName = input("Enter file name to sort: ").lower()
    sortBy = fileName.split()
    folderName = input("Create folder with name: ")
    
    def loadFiles():
        for file in os.listdir(path=currentDir):
            if (file != folderName):
                itemList.append(file)
            
    
    def sortFiles(name):
        matching = []
        for file in itemList:
            termCount = 0
            for term in sortBy:
                
                if term in file.lower():
                    termCount = termCount + 1
                
            if(termCount == len(sortBy)):
                print(file + "\n")
                matching.append(file)
                
        confirm = input("Do you want to move these files? [Y/N]: ")
        
        if (confirm.lower() == "n"):
            print("Move cancelled")
            return
        elif (confirm.lower() == "y"):
            print("Moving...")
                
        if not os.path.exists("C:\\Users\\Kieran\\Files\\Torrents\\Bobs Burgers\\" + folderName):
            os.makedirs("C:\\Users\\Kieran\\Files\\Torrents\\Bobs Burgers\\" + folderName)
        
        for file in matching:
            os.rename("C:\\Users\\Kieran\\Files\\Torrents\\Bobs Burgers\\" + file, "C:\\Users\\Kieran\\Files\\Torrents\\Bobs Burgers\\" + folderName +"\\" + file)
            
        #os.close(0)
        if(confirm.lower() == "y"):
            print("Move complete.")
            
        
        
    loadFiles()
    sortFiles(fileName)
    
    userChoice = input("Exit Show Sorter? [Y/N]").lower()
    if(userChoice == "y"):
        endSession = True
        
