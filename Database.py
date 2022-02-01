import mysql.connector

class Database:
    def __init__(self):
        self.bd = None

    def conectar(self):
        self.bd = mysql.connector.connect(host='localhost',database='LPN3',user='root',password='Sabrina2003')
        db_info = self.bd.get_server_info()
        print("Conectado ao servidor MySQL versão ",db_info)
        return self.bd
    
    def desconectar(self):
        self.bd.close()

       
    