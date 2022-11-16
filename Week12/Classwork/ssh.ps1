# SSH VIDEO CODE
### Commands run in terminal

    ### Find-Module ssh
    ### Find-Module *ssh*
    ### Install-Module Posh-SSH
    ### Get-Command -Module Posh-SSH

# Login to a remote SSH server
# Note: When stuff is in parenthesis it is run first
#New-SSHSession -ComputerName '192.168.6.71' -port 2222 -Credential (Get-Credential sarah.fornaldes)
    ### Get-Command -Module Posh-SSH

<#
#  While loop tp run multiple commands on remote SSH server
while ($TRUE) {
    # Add a prompt to  run commands
    $the_cmd = Read-Host -Prompt "Please enter a command"

    # Run Command on remote SSH server
    #(Invoke-SSHCommand -index 0 'ps -ef').Output
    (Invoke-SSHCommand -index 0 $the_cmd).Output
        ###Get-SSHSession
}  
#>

New-SSHSession -ComputerName '184.171.158.203' -Credential (Get-Credential sarahfornaldes)
Set-SCPItem -ComputerName '184.171.158.203' -Credential (Get-Credential sarahfornaldes) `
-Destination '/Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Classwork/' -Path  '/Users/sarahfornaldes/Desktop/sys320Screenshot.jpeg'
    ### Invoke-SSHCommand -index 4 'ls -l /Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Homework/'  
    ### Get-SSHSession
    ### Remove-SSHSession -SessionId 0 (Do this untill all sessions are closed,  just change zero to your SessionId, you can find those using Get-SSHSession)


        # Make sure to end the ssh session
        ###Remove-SSHSession 

        # To enable ssh: Go to settings,  sharing, turn on and off remote login