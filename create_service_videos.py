import os
import subprocess
import sys
import numpy

os.chdir(r"C:\Users\claym\OneDrive\New Website\assets\media")

print("=" * 70)
print("CREATING VIDEOS FROM IMAGES")
print("=" * 70)

# Try to install moviepy if not available
try:
    import moviepy.editor as mpy
    print("✓ moviepy is available")
except ImportError:
    print("Installing moviepy...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'moviepy', '-q'])
        import moviepy.editor as mpy
        print("✓ moviepy installed")
    except:
        print("⚠️  moviepy installation may have issues")
        import moviepy.editor as mpy

from PIL import Image, ImageDraw, ImageFont

# Video configuration
duration = 5  # 5 seconds per video
fps = 24

video_config = [
    {
        'image': 'python-code.jpg',
        'output': 'python-demo.mp4',
        'title': 'Python Development',
        'subtitle': 'Automation • APIs • Data Processing'
    },
    {
        'image': 'api-architecture.jpg',
        'output': 'api-demo.mp4',
        'title': 'Backend & APIs',
        'subtitle': 'REST APIs • Databases • Security'
    },
    {
        'image': 'frontend-ui.jpg',
        'output': 'frontend-demo.mp4',
        'title': 'Frontend Development',
        'subtitle': 'React • Next.js • Responsive Design'
    },
    {
        'image': 'fullstack-app.jpg',
        'output': 'fullstack-demo.mp4',
        'title': 'Full-Stack Projects',
        'subtitle': 'End-to-End Solutions • Design to Deploy'
    }
]

print("\n🎬 Creating videos...\n")

for config in video_config:
    image_path = config['image']
    output_path = config['output']
    
    if not os.path.exists(image_path):
        print(f"❌ {image_path} not found")
        continue
    
    try:
        print(f"⏳ Creating {output_path}...")
        
        # Load and process image
        img = Image.open(image_path)
        
        # Create a copy with text overlay
        img_with_text = img.copy()
        draw = ImageDraw.Draw(img_with_text, 'RGBA')
        
        # Add semi-transparent overlay
        overlay = Image.new('RGBA', img_with_text.size, (0, 0, 0, 120))
        img_with_text.paste(overlay, (0, 0), overlay)
        
        # Add text
        try:
            title_font = ImageFont.truetype("arial.ttf", 60)
            subtitle_font = ImageFont.truetype("arial.ttf", 30)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # Draw title
        title_bbox = draw.textbbox((0, 0), config['title'], font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (img_with_text.width - title_width) // 2
        draw.text((title_x, 100), config['title'], fill=(255, 255, 255, 255), font=title_font)
        
        # Draw subtitle
        subtitle_bbox = draw.textbbox((0, 0), config['subtitle'], font=subtitle_font)
        subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
        subtitle_x = (img_with_text.width - subtitle_width) // 2
        draw.text((subtitle_x, 200), config['subtitle'], fill=(99, 179, 237, 255), font=subtitle_font)
        
        # Create video clip from image
        clip = mpy.ImageClip(numpy.array(img_with_text)).set_duration(duration)
        clip.write_videofile(output_path, fps=fps, verbose=False, logger=None)
        
        size = os.path.getsize(output_path)
        print(f"✅ {output_path} ({size:,} bytes)\n")
        
    except Exception as e:
        print(f"❌ Error creating {output_path}: {e}\n")

print("=" * 70)
print("VIDEO CREATION COMPLETE!")
print("=" * 70)
