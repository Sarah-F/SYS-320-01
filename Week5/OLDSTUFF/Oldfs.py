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
searchTerm = args.searchTerm

# Check if the argument is a directory (to test on Mac)
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()





# Creates logs function, function sifts through logs
def logs(filename,searchTerm):
    # List to save files
    fList = []

    # Crawl through the provided directory
    for root, subfolders, filenames in os.walk(rootdir):
        for f in filenames:
            #print(root  + "/" + f)
            fileList = root  + "/" + f
            #print(fileList)
            fList.append(fileList)    
        # Creates a csv reader object, stores as f
        contents = csv.reader(f)
        
        # List to store the results
        results = []

        # Loops through each line
        for eachLine in contents:
            # for loop searched for keywords in searchTerms;
            for keyword in searchTerm:
                # Searches for specific keywords
                x = re.findall(r'' + keyword + '', eachLine[1])
                
                for found in x:
                        # Appends new results to results
                        results.append(eachLine)

        return results










# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):
    for f in filenames:
        #print(root  + "/" + f)
        fileList = root  + "/" + f
        #print(fileList)
        fList.append(fileList)

# Start looking through each log file in the directory
keywords = []
# Looks through each log file in directory
for eachFile in fList:
    # Loads cvs and stores spliced results
    results = searchLogCsv.log(eachFile,keywords[1:])

    # Gets keywords from yaml file
    keywords = searchLogYaml.log(searchTerm)

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
                """.format(searchTerm,eachFile, results[1], keywords[0], results[2],results[3], results[5], results[6]))


