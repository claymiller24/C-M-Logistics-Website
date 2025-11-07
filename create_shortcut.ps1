# Get paths
$scriptPath = $PSScriptRoot
$desktopPath = [System.Environment]::GetFolderPath("Desktop")
$websitePath = Join-Path $scriptPath "launch_website.bat"
$iconPath = Join-Path $scriptPath "assets\favicon.ico"

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed! Please install Python 3.x from python.org" -ForegroundColor Red
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
    exit
}

# Convert favicon.svg to .ico if it doesn't exist
if (-not (Test-Path $iconPath)) {
    Write-Host "Creating favicon.ico..."
    try {
        magick convert (Join-Path $scriptPath "assets\favicon.svg") -background none -resize 256x256 $iconPath
    } catch {
        Write-Host "Could not create favicon.ico. Using default icon." -ForegroundColor Yellow
        $iconPath = "shell32.dll,0"
    }
}

# Create shortcut
$shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut("$desktopPath\C&M Logistics Website.lnk")
$shortcut.TargetPath = $websitePath
$shortcut.IconLocation = $iconPath
$shortcut.WorkingDirectory = "C:\Users\claym\OneDrive\New Website"
$shortcut.Save()

Write-Host "Desktop shortcut created! You can now launch the website by double-clicking 'C&M Logistics Website' on your desktop."