import syslogCheck
import re
import importlib
importlib.reload(syslogCheck)

# This function searches the log file and extracts all occurrences of the filename, remote host, the number of bytes sent, and the number of bytes received for each occurrence.
def bytes_sent_bytes_recieved(filename, service, term):

    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        #for loop in sp_results that filters out lowercase qq
        for item in sp_results:
            if bool(re.search(r"qq", item)):
                sp_results.remove(item)
                    #THIS CODE ONLY REMOVES THE WORDS NOT THE LINE/ROW, 
                    #I WENT TO TUTORING BUT WE WERE UNABLE TO FIGURE OUT HOW TO REMOVE THE ENTIRE LINE
                    #TUTOR SUGGEST THE SPLIT MAY BE THE PROBLEM

        # Append the split value to the found list
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4]+ " bytes sent " + sp_results[7] + " bytes recevied ")  #Bytes sent replaces 5 and 6, bytes recieved replaces 7 and 8
        #need to figure ouy how to get rid of proxy closed lines

    # Remove Duplicates by using set
    # and convert the list to a dictionary
    getValue = set(found)

    # Print results
    for eachValue in getValue:

        print(eachValue)

        
# This function searches through the log file and extracts all occurrences of "QQ" files where there is a proxy opened message.
def proxy_opened_message(filename, service, term):

    # Call syslogCheck and return the results
    is_found = syslogCheck._syslog(filename, service, term)

    # found list
    found = []

    # Loop through the results
    for eachFound in is_found:

        # print(eachFound)
        # Split the results
        sp_results = eachFound.split(" ")

        #for loop in sp_results that filters out lowercase qq
        for item in sp_results:
            if bool(re.search(r"qq", item)):
                sp_results.remove(item)

        # Append the split value to the found list
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " through proxy") #Through replaces 4 and 5

    # Remove Duplicates by using set
    # and convert the list to a dictionary
    getValue = set(found)

    # Print results
    for eachValue in getValue:

        print(eachValue)