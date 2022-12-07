### Commands run in terminal

    ### Find-Module ssh
    ### Find-Module *ssh*
    ### Install-Module Posh-SSH
    ### Get-Command -Module Posh-SSH

<#
# List the files in a directory and to export the results to csv file
Get-ChildItem -recurse -Include *.docx,*.xlsx,*.pdf,*.txt -Path ./Documents | Export-Csv -Path '/Users/sarahfornaldes/Desktop/SYS-320-01/Week14/Homework/files.csv'


# Zip the folder
Compress-Archive ./files.csv -Destination '/Users/sarahfornaldes/Desktop/SYS-320-01/Week14/Homework/zippedFilesCsv.zip'
#>

# SCP the files
# Login to a remote SSH server
New-SSHSession -ComputerName '184.171.158.209' -Credential (Get-Credential sarahfornaldes)
Set-SCPItem -ComputerName '184.171.158.209' -Credential (Get-Credential sarahfornaldes) `
-Destination '/Users/sarahfornaldes/Desktop/SYS-320-01/Week14/Homework/scpFolder' -Path '/Users/sarahfornaldes/Desktop/SYS-320-01/Week14/Homework/zippedFilesCsv.zip'
### Get-SSHSession

# Make sure to end the ssh session
### Remove-SSHSession -SessionId 0 (Do this untill all sessions are closed,  just change zero to your SessionId, you can find those using Get-SSHSession)
    
# To enable ssh: Go to settings,  sharing, turn on and off remote login
    

