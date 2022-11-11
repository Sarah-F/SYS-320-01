# Creates random number between 1000-9876 to add to end of EnNob file
$getRand = Get-Random -Maximum 9876 -Minimum 1000

# Copies powershell.exe to my Week11\Homework directory
Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" `
-Destination "C:\Users\sarah.fornaldes\Desktop\SYS-320\Week11\Homework\EnNoB-$getRand.exe"

# Renames copied file.
$newFileName = "C:\Users\sarah.fornaldes\Desktop\SYS-320\Week11\Homework\EnNoB-$getRand.exe"

# Checks if copied file exists
if (Test-Path -Path $newFileName){
    write-host "The File is Found"
}
else{
    write-host "Error"
}