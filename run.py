import http.server
import os

DIRECTORY = "docs"
PORT = 8080

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    directory_index = os.path.join(DIRECTORY, "index.html")

    def translate_path(self, path):
        return http.server.SimpleHTTPRequestHandler.translate_path(self, f"{DIRECTORY}/{path}")
    
with http.server.HTTPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nServer stopped.")
        httpd.server_close()