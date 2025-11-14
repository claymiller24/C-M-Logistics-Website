import subprocess
import sys
import os

print("Checking for FFmpeg installation...")
result = subprocess.run(['where', 'ffmpeg'], capture_output=True, text=True)

if not result.stdout:
    print("\n" + "=" * 70)
    print("FFmpeg not found! Installing FFmpeg via Chocolatey...")
    print("=" * 70)
    
    # Check if Chocolatey is installed
    choco_check = subprocess.run(['where', 'choco'], capture_output=True, text=True)
    
    if choco_check.stdout:
        print("✓ Chocolatey found. Installing FFmpeg...")
        subprocess.run(['choco', 'install', 'ffmpeg', '-y'], shell=True)
    else:
        print("❌ Chocolatey not found.")
        print("\nPlease install FFmpeg manually:")
        print("  1. Download from: https://ffmpeg.org/download.html")
        print("  2. Or use Chocolatey: choco install ffmpeg -y")
        sys.exit(1)
else:
    print("✓ FFmpeg is installed!")
    print(result.stdout[:100])
