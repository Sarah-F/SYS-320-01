import csv, re, yaml

# Creates logs function, function sifts through logs
def logs(term):

    listOfKeywords = []
    # Open the searchTerms.yaml file
    try:
        with open('Task2_searchTerms.yaml', 'r') as yf:
            keywords = yaml.safe_load_all(yf)
    except EnvironmentError as e:
        print(e.strerror)
            
        #Split the etries by the commas
        listOfKeywords = term.split(", ")

    return listOfKeywords
