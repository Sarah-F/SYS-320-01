# Array of websites containing threat intel 
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLs for the rules list
foreach ($u in $drop_urls) {

    # Extract the filename
    # Split the url at the slash, split takes a string and turns it into an array
    $temp = $u.split("/")
    
    # The last element in the array plucked off is the filename 
    $file_name = $temp[-1]

    if (Test-Path $file_name) {
        continue
    } 
    else {
        # Download thhe rules list 
        Invoke-WebRequest -Uri $u -OutFile $file_name
        ### To check if the files downloaded, in terminal type the dir command
    } # Close if statement
} # Close the foreach loop

# Array containing the filename
$input_paths = @('./compromised-ips.txt','./emerging-botcc.rules')

# Extract the IP addresses. 
#b = boundary,d= digit, this command means within these boundaries search for a digit that contains between one and three digit aka  first octet of our ip address
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list. 
Select-String -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value } | Sort-Object | Get-Unique | ` <# Sorts IPs and excludes duplicates  #>
Out-File -FilePath "/Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Homework/ips-bad.tmp"


# Asks for user input,  do they want Windows Firewall rules or IPTable rules. The input by the user will be stored as the value for $var.
$var = Read-host -Prompt "Please enter Windows or IPTables"


switch ($var) {
    IPTables{
        # Get the IP addresses discovered, Loop through and replaace the beginning  of the line with the IPTables syntax
        (Get-Content -Path "ips-bad.tmp") | % `
        { $_ -replace "^","iptables  -A INPUT -s " -replace "$", " -j DROP" } | `
        Out-File -FilePath "/Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Homework/iptables.bash"

        if (Test-Path "/Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Homework/iptables.bash") {
            Write-Host "File Found"
            continue
        } 
        else {
            # If file not created
            Write-Host "Error, File Not Created"
            Exit
        }
    }

    Windows{
        # Get IPs from "ips-bad.tmp", loop through and replace the commands with windows commands
        # https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule?view=windowsserver2022-ps   
        (Get-Content -Path "/Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Homework/ips-bad.tmp") | `
        Foreach-object { $_ -replace "^", "New-NetFirewallRule -DisplayName 'Block Outbound' -Direction Outbound -Profile Any -Action Block -RemoteAddress $_"} | `
        Out-File -FilePath "/Users/sarahfornaldes/Desktop/SYS-320-01/Week12/Homework/WindowsFirewall.ps1"
    }
}