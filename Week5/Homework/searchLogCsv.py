import csv, re, yaml, os, argparse

# Creates logs function, function sifts through logs
def logs(filename,searchTerm):
    # parser
    parser = argparse.ArgumentParser(

        description= "Traverses a directory and find attacks or attempted attacks in web logs.",
        epilog= "Developed by Sarah Fornaldes, 20220924"
    )

    # Commandline argument for the directory and for the searchTerms YAML book.
    parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")
    parser.add_argument("-s", "--searchTerm", required="True", help="traverses searchTerms.yaml")

    # Stores root directory
    rootdir = args.directory
    # Stores search term
    searchTerm = args.searchTerm

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