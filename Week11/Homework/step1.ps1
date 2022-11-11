$getRand = Get-Random -Maximum 9876 -Minimum 1000
Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" `
-Destination "C:\Users\sarah.fornaldes\Desktop\SYS-320\Week11\Homework\EnNoB-$getRand.exe"
$newFileName = "C:\Users\sarah.fornaldes\Desktop\SYS-320\Week11\Homework\EnNoB-$getRand.exe"

if (Test-Path -Path $newFileName){
    write-host "The File is Found"
}
else{
    write-host "Error"
}