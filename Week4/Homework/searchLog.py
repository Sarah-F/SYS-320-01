import re, sys, yaml
import searchLog

# Sifts through logs
def logs(logFile,searchTerm):
    # Opens searchTerms.yaml
        try:
            with open('searchTerms.yaml', 'r') as yf:
                keywords = yaml.safe_load_all(yf)

                # Creates list for the list of keywords to scan
                # #Query the ymal for the terms specified inside
                terms = searchTerm
                
                #Split the etries by the commas
                listOfKeywords = terms.split(", ")
               
                # Opens log file 
                with open(logFile) as f:

                    # Reads file and saves it to a variable
                    contents = f.readlines()

                # Creates list to store results
                results = []

                # Loops through contents list
                for line in contents:

                    # Loops through  keywords
                    for eachKeyword in listOfKeywords:

                        # If the 'line' contains the keyword then it will print
                        # Searches returned results using a regular expression
                        x = re.findall(r''+eachKeyword+'', line)

                        for found in x:
                            # Appends returned keywords to results list
                            results.append(found)

                # Checks if there are any results
                if len(results) == 0:
                    print("No Results")
                    sys.exit(1)

                # Sorts list
                results = sorted(results)

            return results

        except EnvironmentError as e:
            print(e.strerror)

#I tried this but it didn't work
#pip3 install pyyaml
#pip3 install --upgrade pip