# Create commandline parameters to copy a file and place into an evidence directory
param(
    ## In terminal you will be prompted to enter an int
    [Parameter(Mandatory = $true)]
    [int]$reportNo,
    ## In terminal you will be prompted to enter a string
    [Parameter(Mandatory = $true)]
    [string]$filePath

    ## To run the commands via terminal/command line:
    #./grabFile.ps1 -reportNo 101 -filePath ./Documents/Documents/Audits/Commercial_audit_checklist_tool.xlsx
)

# Create a directory with the report number
$reportDir = "rpt$reportNo"

# Creating a new director
mkdir $reportDir

# Copy the file into the new directory
Copy-Item $filePath $reportDir

## RUN THIS COMMAND IN THE COMMAND LINE:
#./grabFile.ps1 -reportNo 101 -filePath ./Documents/Documents/Audits/Commercial_audit_checklist_tool.xlsx
## rpt101 will be created with the Commercial_audit_checklist_tool.xlsx inside it