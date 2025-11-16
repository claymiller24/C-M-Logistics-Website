# Get paths
$scriptPath = $PSScriptRoot
$desktopPath = [System.Environment]::GetFolderPath("Desktop")
$websitePath = Join-Path $scriptPath "launch_website.bat"
$iconPath = Join-Path $scriptPath "assets\favicon.ico"
$appIconSvg = Join-Path $scriptPath "assets\icons\app-icon.svg"
$appIconPng = Join-Path $scriptPath "assets\icons\app-icon-180.png"
${fav32} = Join-Path $scriptPath "assets\icons\favicon-32x32.png"
${fav16} = Join-Path $scriptPath "assets\icons\favicon-16x16.png"
${icon192} = Join-Path $scriptPath "assets\icons\app-icon-192.png"
${icon512} = Join-Path $scriptPath "assets\icons\app-icon-512.png"

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

# Generate app icon PNG (180x180) from SVG if available
try {
    if (Test-Path $appIconSvg) {
        if (-not (Test-Path $appIconPng)) {
            Write-Host "Generating app-icon-180.png from SVG..."
            $null = New-Item -ItemType Directory -Force -Path (Split-Path $appIconPng)
            magick convert $appIconSvg -background none -resize 180x180 $appIconPng
        }
        if (-not (Test-Path ${icon192})) {
            Write-Host "Generating app-icon-192.png..."
            magick convert $appIconSvg -background none -resize 192x192 ${icon192}
        }
        if (-not (Test-Path ${icon512})) {
            Write-Host "Generating app-icon-512.png..."
            magick convert $appIconSvg -background none -resize 512x512 ${icon512}
        }
        if (-not (Test-Path ${fav32})) {
            Write-Host "Generating favicon-32x32.png..."
            magick convert $appIconSvg -background none -resize 32x32 ${fav32}
        }
        if (-not (Test-Path ${fav16})) {
            Write-Host "Generating favicon-16x16.png..."
            magick convert $appIconSvg -background none -resize 16x16 ${fav16}
        }
    }
} catch {
    Write-Host "ImageMagick not available or conversion failed. Using existing icons." -ForegroundColor Yellow
}

# Create shortcut
$shortcut = (New-Object -ComObject WScript.Shell).CreateShortcut("$desktopPath\NCM Solutions Website.lnk")
$shortcut.TargetPath = $websitePath
$shortcut.IconLocation = $iconPath
$shortcut.WorkingDirectory = "C:\Users\claym\OneDrive\New Website"
$shortcut.Save()

Write-Host "Desktop shortcut created! You can now launch the website by double-clicking 'NCM Solutions Website' on your desktop."

<#
# Licensed by Clay Miller
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#>