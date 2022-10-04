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
for eachFile in fList:
    
    # Loads CSV, stores spliced results
    results = searchLogCsv.logs(eachFile,keywords[1:])    

    # Gets keywords from yaml file
    keywords = searchLogYaml.logs(searchT)

    # print out results if there was a match found
    if len(results) > 0:
        for results in results:
            print(
                """
                %s From file %s :
                Arguments: %s
                Hostname: %s
                Name: %s
                Path: %s
                PID: %s
                Username: %s
                """.format(searchT,eachFile, results[1], keywords[0], results[2],results[3], results[5], results[6]))
                # changed serachTerm to searchT

#cd ~/Desktop/SYS-320-01/Week5/Homework
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/ps1
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/Powershell
#python3 Oldfs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs -s/Detections