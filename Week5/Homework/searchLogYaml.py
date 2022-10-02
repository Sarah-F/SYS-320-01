import csv, re, yaml

# Creates logs function, function sifts through logs
def logs(term):

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

    return listOfKeywords
