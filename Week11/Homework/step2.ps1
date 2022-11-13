# Message body
$msg = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."

# Readme.READ created
$readMe = "C:\Users\sarah.fornaldes\Desktop\SYS-320\Week11\Homework\Readme.READ"

# $msg added to $Readme.READ
Write-Output $msg > $readME

# Checks if copied file exists
if (Test-Path -Path $readMe){
    write-host "The File is Found"
}
else{
    write-host "Error"
}
