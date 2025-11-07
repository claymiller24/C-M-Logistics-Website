# C-M-Logistics-Website
My website that showcases my new programming company.

## Features

- Professional and modern design
- Responsive layout (mobile-friendly)
- Service showcase section
- Company information
- Contact details
- Smooth navigation

## How to Launch the Website

### Option 1: Using Python Launcher (Recommended)

Simply run the launcher script:

```bash
python3 launcher.py
```

The script will:
- Start a local web server on port 8000
- Automatically open the website in your default browser
- Keep the server running until you press Ctrl+C

### Option 2: Using Python's Built-in HTTP Server

```bash
python3 -m http.server 8000
```

Then open your browser and navigate to: `http://localhost:8000`

### Option 3: Direct File Opening

You can also open `index.html` directly in your browser by double-clicking the file or using:

```bash
open index.html     # macOS
xdg-open index.html # Linux
start index.html    # Windows
```

## File Structure

```
C-M-Logistics-Website/
├── index.html      # Main HTML file
├── styles.css      # CSS styling
├── launcher.py     # Python launcher script
├── README.md       # This file
└── LICENSE         # License file
```

## Technologies Used

- HTML5
- CSS3
- Python 3 (for the launcher)

## Requirements

- Python 3.x (for the launcher script)
- Any modern web browser (Chrome, Firefox, Safari, Edge)

## License

See LICENSE file for details.
