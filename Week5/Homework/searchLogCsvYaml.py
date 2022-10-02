import csv, re, yaml

# Creates logs function, function sifts through logs
def logs(filename,searchTerm,term):

    listOfKeywords = []
    # Open the searchTerms.yaml file
    try:
        with open('searchTerms.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)
            # Create list for the list of keywords to search
            for eachEntry in keywords:
                for key,value in eachEntry[term].items():
                    listOfKeywords.append(value)

    except EnvironmentError as e:
        print(e.strerror)

    # Opens file and stores it as variable f
    with open(filename) as f:
        
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

    return results, listOfKeywords
