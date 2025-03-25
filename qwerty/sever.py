import socket

host = '127.0.0.1'  # Change to '0.0.0.0' to allow external access
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Server running at http://{host}:{port}/")

while True:
    client, address = server.accept()
    print(f'Connection kim tomonidan {address} orqali qabul qilindi')
    request = client.recv(1024).decode('utf-8')
    print(f"HTTP so‘rov:\n{request}")

    # HTML sahifa
    body = """\
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <title>Socket Server</title>
</head>
<body>
    <h1>Salom, to‘gam! 🚀</h1>
    <p>Bu socket orqali ishga tushgan server!</p>
</body>
</html>
"""

    # HTTP javobi (to'g'ri formatda)
    response = f"""\
HTTP/1.1 200 OK\r
Content-Type: text/html\r
Content-Length: {len(body.encode('utf-8'))}\r
Connection: close\r
\r
{body}"""

    # Javobni yuboramiz
    client.sendall(response.encode("utf-8"))

    client.close()
