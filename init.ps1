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
    $testpath = $folder + "\test.txt"
    $inputpath = $folder + "\input.txt"
    $puzzle1path = $folder + "\puzzle1.py"
    $puzzle2path = $folder + "\puzzle2.py"
    New-Item $testpath
    New-Item $inputpath
    Copy-Item ".\template.py" $puzzle1path
    Copy-Item ".\template.py" $puzzle2path
    code $folder $testpath $inputpath $puzzle1path $puzzle2path
}