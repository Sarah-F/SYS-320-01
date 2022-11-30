# List the files in a directory and
#Get-ChildItem -recurse -Path ./Documents
## -Include allows you to specify files you want to look for 
#Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents
## Get-Member provides you all of the properties for a given cmdlet
#Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents | Get-Member
# List files and print the full path.
## We found FUllName with the Get-Member command, to select it do the following, Select FullName prints out the full name of the file path
#Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents | Select FullName
## To export the results to csv file
Get-ChildItem -recurse -Include *.docx,*.pdf,*.txt -Path ./Documents | Export-Csv -Path files.csv

# Import CSV file
$fileList = Import-Csv -Path ./files.csv -header FullName
## To see if fileList was created
#$fileList

# Loop through the results
foreach ($f in $fileList) {
    Get-ChildItem -Path $f.FullName

}










### COMMENT EXPLANATIONS
#Get... = (no space) commented out code
# List.... = (one hash) = Dwayne comments
## -Include = (two hash = personal comments)