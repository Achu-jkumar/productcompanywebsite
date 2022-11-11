from http.server import HTTPServer,BaseHTTPRequestHandler
content="""
<!DOCTYPE html>
<html>
<head>
<title>Languages</title>
</head>
<body>
    <h1>Python</br>
    Java</br>
    </h1>
</body>
</html>

"""

class myhandler (BaseHTTPRequestHandler):
    def do_GET(self):
        print("Recieved")
        self.send_response(200)
        self.send_header('content-type','text/html','charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address=('',8080)
httpd =HTTPServer(server_address,myhandler)
print("Worked")
httpd.serve_forever()