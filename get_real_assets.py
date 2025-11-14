import urllib.request
import os
import time

os.chdir(r"C:\Users\claym\OneDrive\New Website\assets\media")

print("=" * 70)
print("DOWNLOADING REAL STOCK IMAGES & VIDEOS FOR SERVICES")
print("=" * 70)

# Real stock images - relevant to each service
# Using direct image URLs from Pexels (free, CC0 license)
images = {
    'python-code.jpg': 'https://images.pexels.com/photos/3862618/pexels-photo-3862618.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&dpr=1',  # Code on screen
    'api-architecture.jpg': 'https://images.pexels.com/photos/3888151/pexels-photo-3888151.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&dpr=1',  # Server/network
    'frontend-ui.jpg': 'https://images.pexels.com/photos/3194519/pexels-photo-3194519.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&dpr=1',  # Web design
    'fullstack-app.jpg': 'https://images.pexels.com/photos/3182812/pexels-photo-3182812.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&dpr=1',  # Developer coding
}

print("\n📸 DOWNLOADING IMAGES...")
print("-" * 70)

for filename, url in images.items():
    try:
        print(f'  ⏳ {filename}...')
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(request)
        urllib.request.urlretrieve(url, filename)
        size = os.path.getsize(filename)
        print(f'  ✅ {filename} ({size:,} bytes)')
        time.sleep(0.5)  # Be nice to the server
    except Exception as e:
        print(f'  ❌ {filename}: {str(e)[:50]}')

print("\n🎬 DOWNLOADING VIDEOS...")
print("-" * 70)
print("Downloading tech/development related videos from Pexels...")

# Real stock videos - relevant to tech/development
# These are direct video URLs from Pexels (free, CC0 license)
videos = {
    'python-demo.mp4': 'https://videos.pexels.com/video-files/3945701/3945701-sd_640_360_30fps.mp4',  # Code/programming
    'api-demo.mp4': 'https://videos.pexels.com/video-files/6964062/6964062-sd_640_360_25fps.mp4',  # Tech/server
    'frontend-demo.mp4': 'https://videos.pexels.com/video-files/3571922/3571922-sd_640_360_30fps.mp4',  # Web design
    'fullstack-demo.mp4': 'https://videos.pexels.com/video-files/2024704/2024704-sd_640_360_30fps.mp4',  # Development
}

for filename, url in videos.items():
    try:
        print(f'  ⏳ {filename}...')
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(request)
        urllib.request.urlretrieve(url, filename)
        size = os.path.getsize(filename)
        if size > 100000:  # If larger than 100KB, it's probably valid
            print(f'  ✅ {filename} ({size:,} bytes)')
        else:
            print(f'  ⚠️  {filename} ({size:,} bytes) - file seems small')
        time.sleep(0.5)
    except Exception as e:
        print(f'  ❌ {filename}: {str(e)[:50]}')

print("\n" + "=" * 70)
print("DOWNLOAD COMPLETE!")
print("=" * 70)

# Verify files
print("\n✓ FINAL ASSET VERIFICATION:")
print("-" * 70)
for ext in ['*.jpg', '*.mp4']:
    files = [f for f in os.listdir() if f.endswith(ext.replace('*', ''))]
    if files:
        for f in sorted(files):
            size = os.path.getsize(f)
            print(f"  {f:25} {size:>10,} bytes")
