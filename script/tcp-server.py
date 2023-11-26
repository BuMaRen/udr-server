import os
import logging
from socketserver import TCPServer, BaseRequestHandler
from threading import Thread, Semaphore
logging.basicConfig(filename='./udr-server.log', encoding='utf-8', level=logging.DEBUG)

class MyTCPHandler(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        logging.debug(self.data)
        
def run_tcp_server(port, sema:Semaphore):
    with TCPServer(('localhost', port), MyTCPHandler) as server:
        logging.error(f'监听本地全部ip的{port}号端口')
        server.serve_forever()
    sema.release(1)

if __name__ == "__main__":
    logging.debug('main start')
    ports = os.environ.get('TCP_PORT', None) or '10500'
    port_list = ports.split(',')
    sema = Semaphore(0)
    counter = 0
    for port in port_list:
        t = Thread(target=run_tcp_server, args=[int(port), sema])
        t.start()
        logging.error("1 thread started")
        counter+=1
    while counter > 0:
        sema.acquire()
        counter-=1
    
    
    