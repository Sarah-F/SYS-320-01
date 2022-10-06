import csv, re, yaml

# Creates logs function, function sifts through logs
def logs(filename,searchTerm):
    #print(searchTerm)    SEARCH TERM IS BROKEN
    # Opens file and stores it as variable f
    with open(filename, "r", encoding="UTF-8") as f:
        
        # Creates a csv reader object, stores as f
        contents = csv.reader(f)
        #print(contents)

        # Skips first line
        for _ in range(1): 
            next(contents)
        
        # List to store the results
        results = []

        # Loops through each line
        for eachLine in contents:
            #print(eachLine)
            # for loop searched for keywords in searchTerms;
            for keyword in searchTerm:
                # Searches for specific keywords
                x = re.findall(r'' + keyword + '',''.join(eachLine[1]))
                #print(x)
                for found in x:
                    args = eachLine[1]
                    host = eachLine[2]
                    name = eachLine[3]
                    path = eachLine[4]
                    pid = eachLine[5]
                    user = eachLine[6]
                    print(
                        """
                        Arguments: {}
                        Hostname: {}
                        Name: {}
                        Path: {}
                        Pid: {}
                        Username: {}
                        """.format(args, host, name, path, pid, user, "*" * 60))