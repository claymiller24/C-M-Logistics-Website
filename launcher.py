#!/usr/bin/env python3
"""
Simple web server launcher for C&M Logistics Website
This script starts a local web server to view the website in a browser.
"""

import http.server
import socketserver
import webbrowser
import sys
import os
import errno

PORT = 8000

def main():
    """Start the web server and open the browser"""
    
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("=" * 60)
            print("C&M Logistics Website Server")
            print("=" * 60)
            print(f"\nServer started at http://localhost:{PORT}")
            print(f"\nOpening website in your default browser...")
            print(f"\nPress Ctrl+C to stop the server\n")
            print("=" * 60)
            
            # Open the browser
            webbrowser.open(f"http://localhost:{PORT}")
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            print(f"\nError: Port {PORT} is already in use.")
            print("Please close any other applications using this port or use a different port.")
            sys.exit(1)
        else:
            raise

if __name__ == "__main__":
    main()
