from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # リクエストヘッダーを表示
        print("Received request with headers:")
        for header, value in self.headers.items():
            print(f"{header}: {value}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")

if __name__ == "__main__":
    server_address = ("", 8080)  # ポート番号は適宜変更してください
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print(f"Server started on port {server_address[1]}")
    httpd.serve_forever()
