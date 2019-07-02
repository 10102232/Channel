import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen(5)


while 1:
    conn, addr = sk.accept()
    data = conn.recv(9000)
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # conn.send(b'o98k')
    with open("test.html", "rb") as f:
        conn.send(f.read())
    conn.close()
