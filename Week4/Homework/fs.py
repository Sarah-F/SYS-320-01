# File to traverse a given directory and it's subdirectories and retrieve all the files.
import os, argparse, searchLog

# parser
parser = argparse.ArgumentParser(

    description= "Traverses a directory and find attacks or attempted attacks in web logs.",
    epilog= "Developed by Sarah Fornaldes, 20220924"
)

# Commandline argument for the directory and for the searchTerms YAML book.
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
parser.add_argument("-s", "--searchTerm", required="True", help="traverses searchTerm.yaml")

# Parse the arguments
args = parser.parse_args()
# Stores root directory
rootdir = args.directory
# Stores search term
searchTerm = args.searchTerm

# In our story, we will traverse a directory

# Check if the argument is a directory (to test on Mac)
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        #print(root  + "/" + f)
        fileList = root  + "/" + f
        #print(fileList)
        fList.append(fileList)

# Looks through each log file in directory
for eachFile in fList:
    # check each for the specified attacks
    check = searchLog.logs(eachFile,searchTerm)

    # Creates results list, puts check into results list
    results = []
    print(check)
    # Grabs URL, Status Code and Bytes
    for eachFound in check:
        # Split results
        attack_cheque = eachFound.split(" ")
        results.append( "\t URL: " + attack_cheque[6] + " Status Code: " + attack_cheque[8] + " File Size (Bytes): " + attack_cheque[9])

    # sets results
    results = set(results)

    #prints results
    for eachValue in results:
        # Print
        print(eachValue)

# STUFF TO KNOW FOR USING MAC
# Vs code file path: cd ~/Desktop/SYS-320-01/Week4/Classwork
# to  run bin ./timeliner.bin timeline.body# to enter tmp directory
# python3 fs.py -d/tmp