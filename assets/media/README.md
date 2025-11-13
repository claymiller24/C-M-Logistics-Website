# Media assets and how to create videos/images for the site

This folder contains guidance and small SVG illustrations you can use on the site. Creating real photo/video assets requires a camera or screen capture tool (e.g., OBS) and optionally FFmpeg for trimming/encoding.

Recommended workflow to create a short promo video (30–60s) showing coding/demo:

1. Record with OBS (free, cross-platform)
   - Set base resolution to 1920x1080
   - Capture a window (your editor, terminal, or browser demo)
   - Add a webcam source if you want presenter footage
   - Save as MKV or MP4

2. Trim and compress with FFmpeg (example)

```powershell
# Trim 5s..65s and re-encode H.264, mobile-friendly
ffmpeg -i input.mkv -ss 00:00:05 -to 00:01:05 -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -movflags +faststart demo.mp4
```

3. Generate a poster image (thumbnail)

```powershell
ffmpeg -i demo.mp4 -ss 00:00:03 -vframes 1 poster.jpg
```

4. Upload the `demo.mp4` and `poster.jpg` to the `assets/media/` folder (or an external CDN) and reference them in `index.html`:

```html
<video controls poster="/assets/media/poster.jpg" width="960">
  <source src="/assets/media/demo.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
```

Image ideas and where to get them:
- Use the included SVGs (`developer-hero.svg`, `code-illustration.svg`) for hero and examples.
- Unsplash / Pexels for royalty-free photos of developers, workspaces, and laptops.
- For consistent style, convert photos to B/W and overlay your accent color.

Accessibility and performance tips:
- Use `<video>` with a small MP4 (H.264) and a poster image.
- Defer loading with the `loading="lazy"` attribute on large images.
- Provide descriptive `alt` text for images and captions for videos.

If you'd like, I can:

- Create a short demo video for you (screen recordings require you to grant/upload footage — I can provide a script to stitch clips together using FFmpeg), or
- Generate additional SVG banners and thumbnails and wire them into the site right now.

Tell me which option you prefer and I’ll continue.

## Note about the demo video used on the site

The homepage includes a demo player that points to `/assets/media/demo.mp4` and uses `poster.svg` as a poster.
If you haven't added a `demo.mp4` file to this folder the site will show a poster image and a small download link instead.

To add a demo video, place an MP4 named `demo.mp4` in this folder (H.264 video, AAC audio is widely compatible). Example FFmpeg command is included above.
