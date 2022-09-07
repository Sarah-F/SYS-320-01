# Create and interfacce to search through syslog files ,#logCheck in video
import re, sys, yaml

# Open the Yaml file
try:
    
    with open('searchTerms.yaml', 'r') as yf:
        keywords = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strrerror)

def _syslog(filename, service, term):

    # Query the yaml file for the term or direction and
    # retrieve the strings to searchs on
    # terms = keywords['apache']['php']
    terms = keywords[service][term]


    listOfKeywords = terms.split(",")

    # Open a file, with open makes python close a file if something goes wrong
    with open(filename) as f:
    
        # read in the file and save it to a variable
        contents = f.readlines()

    # Lists to store the results
    results = []
    
    # Loop through the list returned. Each element is a line from the smallSyslog file 
    for line in contents:

        # Loops through keywords
        for eachKeyword in listOfKeywords:
    
            # If the 'line' contains the keyword then it will print
            #if eachKeyword in line: #old line of code
            # Searches returned results using a regular expression
            x = re.findall(r''+eachKeyword+'', line)    
            
            for found in x:
                # Append the returned keywords to the results list
                results.append(found)

    # Check to see if there are results
    if len(results) == 0:
        print("No Results")
        sys.exitt(1)
        
    # Sort the list
    results = sorted(results)
    
    return results
    #print(x)