# File to traverse a given directory and it's subdirectories and retrieve all the files.
import os, argparse, csv, re

# parser
#parser = argparse.ArgumentParser(
#
#    description= "Traverses a directory and builds a forensic body file",
#    epilog= "Developed by Sarah Fornaldes, 20221001"
#)
#
## Add argument to pass to the fs.py program
#parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
#
## Parse the arguments
#args = parser.parse_args()

#rootdir = args.directory
rootdir = input("Please enter the directory path: ")



# Check if the argument is a directory (to test on Mac, possible directory is ~/Applications)
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

# Creates eachOpen function
def eachOpen(filename,searchTerms):
    # Opens file and stores it as variable f
    with open(filename) as f:
        # Creates a csv reader object
        contents = csv.reader(f)
        # Skips the first 9 lines of code, it is file metadata that we don't need
        for _ in range(9): 
            # Returns the next item inside the contents list
            next(contents)
            # Iterates over contents
        for eachLine in contents:
            # for loop searched for keywords in searchTerms;
            for keyword in searchTerms:
                # Searches for specific keywords
                x = re.findall(r'' + keyword + '', eachLine[2])
                for _ in x:
                    print(
                """
                %s From file %s :
                Arguments: %s
                Hostname: %s
                Name: %s
                Path: %s
                PID: %s
                Username: %s
                """)

for eachFile in fList:
    eachOpen(eachFile)