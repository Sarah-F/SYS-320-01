import csv, re, yaml

# Creates logs function, function sifts through logs
def logs(term):

    listOfKeywords = []
    # Open the searchTerms.yaml file
    try:
        with open('searchTerms.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)
    except EnvironmentError as e:
        print(e.strerror)

            # Creates list for the list of keywords to scan
            # #Query the ymal for the terms specified inside
            
            #Split the etries by the commas
        listOfKeywords = term.split(", ")


            # Create list for the list of keywords to search
            #12#for eachEntry in keywords:
                #13#for key,value in eachEntry[term].items():
                #14#    listOfKeywords.append(value)

    #except EnvironmentError as e:
    #    print(e.strerror)

    return listOfKeywords
