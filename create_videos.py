import subprocess
import os

os.chdir(r"C:\Users\claym\OneDrive\New Website\assets\media")

# Videos to create with their descriptions
videos = [
    ('python-demo.mp4', 'Python Development', 'Automation, APIs, Data Processing'),
    ('api-demo.mp4', 'Backend & APIs', 'REST APIs, Databases, Security'),
    ('frontend-demo.mp4', 'Frontend Development', 'React, Next.js, Responsive Design'),
    ('fullstack-demo.mp4', 'Full-Stack Projects', 'End-to-End Solutions'),
]

for video_file, title, subtitle in videos:
    # Create a simple video using FFmpeg
    drawtext1 = f"drawtext=text='{title}':fontsize=80:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2-100"
    drawtext2 = f"drawtext=text='{subtitle}':fontsize=40:fontcolor=lightblue:x=(w-text_w)/2:y=(h-text_h)/2+100"
    
    cmd = [
        'ffmpeg', '-f', 'lavfi', '-i', 'color=c=black:s=1280x720:d=5',
        '-vf', f"{drawtext1}, {drawtext2}",
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-y', video_file
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=15, text=True)
        if os.path.exists(video_file):
            size = os.path.getsize(video_file)
            print(f'✓ Created {video_file} ({size} bytes)')
        else:
            print(f'✗ Failed to create {video_file}')
            if result.stderr:
                print(f'  Error: {result.stderr[:200]}')
    except FileNotFoundError:
        print(f'✗ FFmpeg not found. Install FFmpeg to create videos.')
        break
    except Exception as e:
        print(f'✗ Error creating {video_file}: {e}')
