import os
from socketserver import TCPServer, BaseServer, BaseRequestHandler
from threading import Thread, Semaphore

class MyTCPHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(self.data)
        
def run_tcp_server(port, sema:Semaphore):
    with TCPServer(('localhost', port), MyTCPHandler) as server:
        print(f'监听本地全部ip的{port}号端口')
        server.serve_forever()
    sema.release(1)



if __name__ == "__main__":
    ports = os.environ.get('TCP_PORT', None) or '10500'
    port_list = ports.split(',')
    sema = Semaphore(0)
    counter = 0
    for port in port_list:
        t = Thread(target=run_tcp_server, args=[port, sema])
        t.start()
        counter+=1
    while counter > 0:
        sema.acquire()
        counter-=1
    
    
    