import socket
HOST = ''              # Endereco IP do Servidor
PORT = 8888            # Porta do SO.
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg.decode())
    print ('Finalizando conexao do cliente', cliente)
    con.close()
