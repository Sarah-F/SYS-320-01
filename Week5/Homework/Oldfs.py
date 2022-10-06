# File to traverse a given directory and it's subdirectories and retrieve all the files.
import os, argparse, searchLogCsv, searchLogYaml, csv, re

# parser
parser = argparse.ArgumentParser(

    description= "Traverses a directory and find attacks or attempted attacks in web logs.",
    epilog= "Developed by Sarah Fornaldes, 20220924"
)

# Commandline argument for the directory and for the searchTerms YAML book.
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--searchTerm", required="True", help="traverses searchTerms.yaml")

# Parse the arguments
args = parser.parse_args()
# Stores root directory
rootdir = args.directory
# Stores search term
searchT = args.searchTerm
#print(searchT)

# Check if the argument is a directory
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# save files to list
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        fileList = root  + "/" + f
        fList.append(fileList)    
    
# Looks through each log in the directory
keywords = []

#loops through each file in flist
for eachFile in fList:
    #print(eachFile)
    # Loads CSV, stores spliced results 
    results = searchLogCsv.logs(eachFile,searchT)    
    #print(results)
    #print(searchT)

for keyVal in keywords:
    for key, value in keyVal.items():
        types = value['ref']
        terms = value['detect']
        searchT = terms.split(",")
        print("Attack Description: " + types)

        for file in fList:
            searchLogCsv.logs(eachFile,searchT)







    # Gets keywords from yaml file
    #keywords = searchLogYaml.logs(searchT)
    #print(keywords)

    # print out results if there was a match found
    #if len(results) > 0:
        #for results in results:
    #print(results)
        #%s From file %s :
        #"""
        #Arguments: %s
        #Hostname: %s
       # Name: %s
        #Path: %s
        #Pid: %s
        # # Username: %s
       # """.format(results[0], results[1], results[2],results[3], results[4], results[5]))
                
                #""".format(searchT,eachFile, keywords[0], (results[1], results[2],results[3], results[4], results[5], results[6]))

#cd ~/Desktop/SYS-320-01/Week5/Homework
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/Powershell
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/powershell.exe
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/Detections
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/searchTerms.yaml