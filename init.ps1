[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [String]
    $year,
    [Parameter(Mandatory=$true)]
    [String]
    $day
)

$folder = ".\" + $year + "\" + $day
if(-not (Test-Path -Path $folder))
{
    mkdir -Path $folder
    New-Item ($folder + "\test.txt")
    New-Item ($folder + "\input.txt")
    Copy-Item ".\template.py" ($folder + "\puzzle1.py")
    Copy-Item ".\template.py" ($folder + "\puzzle2.py")
}