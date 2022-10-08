# File to traverse a given directory and it's subdirectories and retrieve all the files.
import os, argparse, searchLogCsv, searchLogYaml, csv, re, yaml

# parser
parser = argparse.ArgumentParser(

    description= "Traverses a directory and find attacks or attempted attacks in web logs.",
    epilog= "Developed by Sarah Fornaldes, 20220924"
)

# Commandline argument for the directory and for the searchTerms YAML book.
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

# Parse the arguments
args = parser.parse_args()
# Stores root directory
rootdir = args.directory
# Stores search term
#searchT =[args.searchTerm]
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
    
with open('searchTerms.yaml', 'r') as yf:
    keywords = yaml.safe_load_all(yf)
    
    # loops through key words, prints attack desription
    for keyVal in keywords:
        #print(keyVal.items())
        for key, value in keyVal.items():
            types = value['ref']
            terms = value['detect']
            searchT = terms.split(",")
            print("Attack Description: " + types)

            for file in fList:
                searchLogCsv.logs(file,searchT)

#cd ~/Desktop/SYS-320-01/Week5/Homework
#python3 fs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs
#python3 fs.py -d/Users/sarahfornaldes/Desktop/SYS-320-01/Week5/logs > results.txt