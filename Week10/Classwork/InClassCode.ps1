# Get a list of running processes

# Get list of members
#Get-process | get-member 

# Get a list of processes: name, id, patj
#Get-process | Select-Object ProcessName, id, Path

# Sace the output to a CSV file. ` continues command on next line (can use between -Path and C -> -Path ` C:\Users)
#Get-process | Select-Object ProcessName, id, Path | Export-csv -Path "C:\Users\sarah.fornaldes\Desktop\SYS320\Week10\Classwork\processes.csv"

#this is a variable
#$outputName = "C:\Users\sarah.fornaldes\Desktop\SYS320\Week10\Classwork\services.csv"
# go test if the file exists code
#$outputName1 = "C:\Users\sarah.fornaldes\Desktop\SYS320\Week10\Classwork\services.csvs"

# System Services 
#Get-service | get-member
#Get-service | select-object Status, Name, DisplayName, BinaryPathName | Export-csv -Path $outputName

$outputName = "C:\Users\sarah.fornaldes\Desktop\SYS320\Week10\Classwork\runningServices.csv"

# Get a list of running services
Get-service | Where-Object { $_.Status -eq "Running" } | Export-csv -Path $outputName
#Get-service | Where-Object { $_.Status -eq "Stopped" }

#Check to see if the file exists
if ( Test-Path $outputName ){
    write-host -backgroundcolor "Green" -foregroundcolor "white" "Services file was created!"
} else {
    write-host -backgroundcolor "red" -foregroundcolor "white" "Services file was not created!"
}

#if ( Test-Path $outputName1 ){
#    write-host -backgroundcolor "Green" -foregroundcolor "white" "Services file was created!"
#} else {
#    write-host -backgroundcolor "red" -foregroundcolor "white" "Services file was not created!"
#}