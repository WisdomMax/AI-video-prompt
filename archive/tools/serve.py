#!/usr/bin/env python3
"""
AI Video Prompt Archive Web Server
Serves the web gallery on localhost with auto browser launch.
"""

import os
import sys
import webbrowser
import http.server
import socketserver
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PORT = 8088

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def do_GET(self):
        # Redirect root to /web/index.html
        if self.path in ("/", "/index.html"):
            self.send_response(302)
            self.send_header("Location", "/web/index.html")
            self.end_headers()
            return
        super().do_GET()

def start_server():
    os.chdir(str(BASE_DIR))
    handler = CustomHTTPRequestHandler
    
    # Try finding an open port if 8088 is occupied
    current_port = PORT
    for _ in range(10):
        try:
            with socketserver.TCPServer(("", current_port), handler) as httpd:
                url = f"http://localhost:{current_port}/web/index.html"
                print(f"✨ AI Video Prompt Archive Web Gallery running at: {url}")
                print("Press Ctrl+C to stop.")
                webbrowser.open(url)
                httpd.serve_forever()
                break
        except OSError:
            current_port += 1

if __name__ == "__main__":
    start_server()
