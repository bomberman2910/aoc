[CmdletBinding()]
param (
    [Parameter(Mandatory=$true)]
    [String]
    $year,
    [Parameter(Mandatory=$true)]
    [String]
    $day
)

git add .

git commit -m ("Added " + $year + " Day " + $day)

git push