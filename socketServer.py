'''
Created on Feb 23, 2012

@author: drazic_1
'''
import SocketServer
import sqlite3


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    conn = sqlite3.connect('./static/tokens')
    c = conn.cursor()
        
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} ha escrito".format(self.client_address[0])
        print 'Mensaje recibido de usuario: ', self.data
        #usr_points contains an array with a tuple with the points (integer)
        usr_points = None
        usr_id = None
        # just send back the same data, but upper-cased
        if "<policy-file-request/>" in self.data:
            print 'Usuario conectado con datos: ', self.request.getpeername()
            self.request.sendall('<cross-domain-policy><allow-access-from domain="*" to-ports="2729" secure="false"/></cross-domain-policy>')
        elif "ConnectedHere!" in self.data:
            print 'Conectado en el servidor'
            #self.request.sendall('ConnectedOK')
        elif "$ClosingConnection$" in self.data:
            self.request.close()
            print 'Connection Closed'
        #Buscamos $$$$#$ en todos los mensajes porque asi hemos indicado que es un mensaje interno del programa. Se elige ese codigo porque 
        #se supone que no aparecera en ningun mensaje de los que el usuario coma y por tanto no podra confundirse
        elif "$userPoints#" in self.data:
            data_split=self.data.rpartition("$$$$#")
            usr_id=data_split[0]
            print 'El usuario ', usr_id, ' quiere saber sus puntos'
            usr_points = self.get_points(usr_id)
            self.request.sendall(str(usr_points[0][0]))
        elif "$$$$#" in self.data:
            data_split=self.data.partition("$$$$#")
            usr_id=data_split[0]
            data_split2=data_split[2].partition("$$$$#")
            message = data_split2[0]
            msg_id = data_split2[2]
            print 'El usuario ', usr_id, ' se ha intentado comer el mensaje', msg_id, ' con contenido: ',message 
            can_eat=self.check_last_mssg(usr_id,msg_id)
            if not can_eat:
                usr_points = self.get_points(usr_id)
                points = usr_points[0][0]+len(self.data)
                print'El usuario ', usr_id, 'se queda con ', points, ' puntos'
                self.set_points(usr_id,points)
                self.set_last_mssg(usr_id,msg_id)
                self.request.sendall(str(points))
                print 'El mensaje se puede comer'   
            else:
                print 'El mensaje no se puede comer'   
                self.request.sendall("Demasiado tarde..." + can_eat[0][0] +" ya se ha comido este mensaje.")
                   
        else:
            print 'Caso no contemplado'
            self.request.sendall("Caso no contemplado")
                        
    
    
    def get_points(self, user_id):        
        self.c.execute('select points from tokens where user_id=?', (user_id,))
        try:
            points = self.c.fetchall()
            #points will be empty list if the user has not been saved before
            if not points: 
                print 'El usuario no esta en la base de datos'
            else:
                print 'El usuario ', user_id, ' tiene ', points, ' puntos'    
        except sqlite3.Error, e:
            print "An error occurred:", e.args[0]  
        return points          

    def set_points(self, user_id, points):
        self.c.execute('UPDATE tokens SET points = ? WHERE user_id=?', (points,user_id,))
        self.conn.commit()
        print 'Puntos del usuario ',user_id, 'actualizados a ', points 

    def check_last_mssg(self, user_id, mssg_id):
        self.c.execute('select user_name from tokens where user_id=? and last_mssg_id=?', (user_id,mssg_id,))
        try:
            user=self.c.fetchall()
            if not user:
                print 'El mensaje no se ha comido antes'
            else:
                print 'Este mesnaje ya se ha comido antes por ',user[0][0]  
        except sqlite3.Error, e:
            print "An error occurred:", e.args[0]            
        return user
     
    def set_last_mssg(self, user_id, mssg_id):
        self.c.execute('UPDATE tokens SET last_mssg_id = ? WHERE user_id=?', (mssg_id,user_id,))
        self.conn.commit()  
        print 'Ultimo mensaje comido por el usuario', user_id, 'actualizado a ', mssg_id 
         
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 2729

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()