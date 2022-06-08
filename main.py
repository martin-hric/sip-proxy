
# main proxy
# sipfullproxy.py stiahnute z https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py
# CREDITS https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py
# upravene a odbugovane podla vlastnej potreby
# Martin Hric
# ID: 111696

import sipfullproxy
import socket
import socketserver
import logging
import time

HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    logging.info(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), sipfullproxy.UDPHandler)
    print(f"spustam server na {ipaddress} ...")
    server.serve_forever()
