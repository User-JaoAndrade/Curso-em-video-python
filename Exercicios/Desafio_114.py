"""
Crie um código python que teste se o site PUDIM está acessivel
pelo computador usado
"""

import socket

try:
    # Tenta estabelecer uma conexão com o endereço www.google.com na porta 80 (HTTP)
    socket.create_connection(("www.pudim.com.br", 80), timeout=5)
    print("Conexão estabelecida")
except OSError:
    print("Sem Conexão")
