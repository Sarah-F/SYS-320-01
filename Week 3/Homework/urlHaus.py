# imports csv and re
# Added import re
import csv
import re
# Creates urlHausOpen function
# Changed function "ur1HausOpen" to "urlHausOpen"
def urlHausOpen(filename,searchTerms):
    # Opens file and stores it as variable f
    # Changed while to with
    # Removed '' from filename / removed quotation marks from around filename
    with open(filename) as f:
        # Creates a csv reader object
        # Changed .review to .reader
        # Changed filename to f since its the variable we declaired in line above 
        # Removed one of the = in the == , 
        contents = csv.reader(f)
        # Skips the first 9 lines of code, it is file metadata that we don't need
        for _ in range(9): 
            # Returns the next item inside the contents list
            next(contents)
            # Iterates over contents
            # Changed order of code, this line was nested in the for keyword in searchTerms loop
        for eachLine in contents:
            # for loop searched for keywords in searchTerms;
            for keyword in searchTerms:
                # Searches for specific keywords
                # Changed r+keyword+ to keyword
                x = re.findall(r'' + keyword + '', eachLine[2])
                # Prints information about the match
                for _ in x:
                    # Don't edit this line. It is here to show how it is possible
                    # to remove the "tt" so programs don't convert the malicious
                    # domains to links that an be accidentally clicked on.
                    the_url = eachLine[2].replace("http","hxxp")
                    the_src = eachLine[7] #changed 4 to 7
                    # added %s to the ends of lines 25 and 26
                    # added %s to the begining of line 27; changed ,format to % ; changed "*"+ to "~"*
                    print("""
                        URL: %s
                        Info: %s 
                        %s """ % (the_url, the_src,"~"*60)) 

#What I did:
#Fixed indentation