import re, sys, yaml
import searchLog

# Sifts through logs
def logs (logFile,searchTerm):
    # Opens searchTerms.yaml
        try:
            with open('searchTerms.yaml', 'r') as yf:
                keywords = yaml.safe_load_all(yf)

                # Creates list for the list of keywords to scan
                listOfKeywords = []
                for eachEntry in keywords:
                    for key,value in eachEntry[searchTerm].items():
                        listOfKeywords.append(value)
                
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

                        # Searches and returns results
                        x = re.findall("%s" %eachKeyword, line)


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