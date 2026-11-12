from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # แยกพารามิเตอร์จาก URL
        parsed_path = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed_path.query)
        msg = params.get('msg', ['Hello, World! V2'])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"<html><body><h1>{msg}</h1></body></html>".encode('utf-8'))

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        print(f"POST received: {body}")

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"<html><body><h1>POST received</h1><p>{body}</p></body></html>".encode('utf-8'))

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleServer)
    print("Server running on port 8000...")
    httpd.serve_forever()