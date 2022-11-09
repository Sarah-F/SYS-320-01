# Send an email using powershell

# To create an array
$toSend = @('d@champlain.edu', 'ston@champlain.edu', 'duns@champlain.edu')
# Message body
$msg = "Hello"

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
