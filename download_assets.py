import urllib.request
import os
import subprocess

os.chdir(r"C:\Users\claym\OneDrive\New Website\assets\media")

print("=" * 60)
print("Downloading High-Quality Stock Images")
print("=" * 60)

# High-quality free stock images from Unsplash
images = {
    'python-code.jpg': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=1200&h=900&fit=crop&q=80',
    'api-architecture.jpg': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=900&fit=crop&q=80',
    'frontend-ui.jpg': 'https://images.unsplash.com/photo-1633356122544-f134324ef6db?w=1200&h=900&fit=crop&q=80',
    'fullstack-app.jpg': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=1200&h=900&fit=crop&q=80',
}

for filename, url in images.items():
    filepath = filename
    try:
        print(f'\nDownloading {filename}...')
        urllib.request.urlretrieve(url, filepath)
        size = os.path.getsize(filepath)
        print(f'✓ Downloaded {filename} ({size:,} bytes)')
    except Exception as e:
        print(f'✗ Failed to download {filename}: {e}')

print("\n" + "=" * 60)
print("Creating Demo Videos")
print("=" * 60)

# Create demo videos with FFmpeg
videos = [
    ('python-demo.mp4', 'Python Development', 'Automation, APIs, Data Processing'),
    ('api-demo.mp4', 'Backend & APIs', 'REST APIs, Databases, Security'),
    ('frontend-demo.mp4', 'Frontend Development', 'React, Next.js, Responsive Design'),
    ('fullstack-demo.mp4', 'Full-Stack Projects', 'End-to-End Solutions'),
]

for video_file, title, subtitle in videos:
    drawtext1 = f"drawtext=text='{title}':fontsize=80:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-80"
    drawtext2 = f"drawtext=text='{subtitle}':fontsize=40:fontcolor=lightblue:x=(w-text_w)/2:y=(h-text_h)/2+80"
    
    cmd = [
        'ffmpeg', '-f', 'lavfi', '-i', 'color=c=black:s=1280x720:d=5',
        '-vf', f"{drawtext1}, {drawtext2}",
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-y', video_file
    ]
    
    try:
        print(f'\nCreating {video_file}...')
        result = subprocess.run(cmd, capture_output=True, timeout=20, text=True)
        if os.path.exists(video_file):
            size = os.path.getsize(video_file)
            print(f'✓ Created {video_file} ({size:,} bytes)')
        else:
            print(f'✗ Failed to create {video_file}')
    except FileNotFoundError:
        print(f'✗ FFmpeg not found. Please install FFmpeg:')
        print(f'   Download from: https://ffmpeg.org/download.html')
        break
    except Exception as e:
        print(f'✗ Error creating {video_file}: {e}')

print("\n" + "=" * 60)
print("Download and Video Creation Complete!")
print("=" * 60)
