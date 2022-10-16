import os, sys, argparse, paramiko, yaml
from getpass import getpass

# parser
parser = argparse.ArgumentParser(

    description= "Traverses a directory and builds a forensic body file",
    epilog= "Developed by Sarah Fornaldes, 20221012"
)

# Add argument to pass to the fs.py program
parser.add_argument("-d", "--directory", required="True", help="Directory that you want to traverse.")

# Parse the arguments
args = parser.parse_args()
# Stores root directory
rootdir = args.directory

# Check if the argument is a directory (to test on Mac, possible directory is ~/Applications)
if not os.path.isdir(rootdir):
    print("Invalid directory => {}".format(rootdir))
    exit()

# List to save files
fList = []

# Crawl through the provided directory
for root, subfolders, filenames in os.walk(rootdir):

    for f in filenames:

        #print(root  + "/" + f)
        fileList = root  + "/" + f
        #print(fileList)
        fList.append(fileList)

with open('Task2_searchTerms.yaml', 'r') as yf:
    keywords = yaml.safe_load_all(yf)
    
    # loops through key words, prints attack desription
    for keyVal in keywords:
        #print(keyVal.items())
        for key, value in keyVal.items():
            cmds = value['cmd']
            commands = cmds.split(",")
            print(commands)


def statFile(toStat):

    # i is going to be the variable used for each of the metadata elements
    i = os.stat(toStat==False) #deleted symlinks

    # mode
    mode = i[0] 
    
    #inode
    inode=i[1]

    # uid
    uid = i[4]

    # gid
    gid = i[5]

    # filesize
    fsize = i[6]

    # access  time
    atime = i[7]

    # modification time
    mtime = i[8]

    # ctime => windows is the birth of the file, when it was created
    # unix it is when attributes of the file changes
    ctime = i[9]
    crtime = i[9]

    print("0|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(toStat, inode, mode, uid, gid, fsize, atime, mtime, ctime, crtime))

for eachFile in fList:
    statFile(eachFile)


# STUFF TO KNOW FOR USING MAC
# Vs code file path: cd ~/Desktop/SYS-320-01/Week6/Homework
# to run bin ./timeliner.bin timeline.body
# to enter tmp directory: python3 fs.py -d/tmp

#Week 4 Classwork fs.py file modified for this assignment