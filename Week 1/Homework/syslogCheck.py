# Create and interfacce to search through syslog files
import re, sys

def _syslog(filename, listOfKeywords):

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