import csv, re, yaml, os

# Creates logs function, function sifts through logs
def logs(filename,searchTerm):

    # Opens file and stores it as variable f
    #with open(filename) as f:
    stuff = stuff
    # Stores root directory
    rootdir = stuff.directory


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