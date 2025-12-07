#!/usr/bin/python3
"""
A simple API built using Python's http.server module.
Supports basic GET routes and returns text or JSON data.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom handler to manage API endpoints"""

    def do_GET(self):
        """Handle GET requests"""

        # --- Root endpoint "/" ---
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # --- /status endpoint ---
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # --- /data endpoint (JSON response) ---
        elif self.path == "/data":
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(sample_data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
            return

        # --- /info endpoint (extra JSON endpoint) ---
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            json_data = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
            return

        # --- Undefined endpoints → 404 error ---
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
            return


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server on port 8000"""
    server_address = ("", 8000)  # listen on all interfaces
    httpd = server_class(server_address, handler_class)

    print("Starting server on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
