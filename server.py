import os
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

class DualStackServer(HTTPServer):
    address_family = socket.AF_INET6

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            instance_id = os.getenv('CYCLE_INSTANCE_ID', 'unknown')
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(instance_id.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('::', 8080)  # IPv6 wildcard address
    httpd = DualStackServer(server_address, Handler)
    try:
        httpd.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)  # allow IPv4
    except (OSError, AttributeError):
        pass
    print("Starting server on [::]:8080 (IPv6 + IPv4 mapped)...")
    httpd.serve_forever()
