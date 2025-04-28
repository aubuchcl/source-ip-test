import os
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

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
    server_address = ('', 8080)  # Bind all available addresses
    httpd = HTTPServer(server_address, Handler)
    try:
        httpd.socket.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
    except (OSError, AttributeError):
        # Either IPv6 is not available or socket option is not supported
        pass
    print("Starting server on all interfaces (IPv4/IPv6 where available)...")
    httpd.serve_forever()
