import socket
import getopt
import sys
import logging
import random
import json
import array
import pickle
import time


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


class UdpClientServer(object):
    UdpIp = '127.0.0.1'
    UdpPort = 5008
    UdpServerPort = 50010

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def client(self):
        log.info("sending data")
        rand = random.Random()
        i =0
        while True:
            time.sleep(0.001)
            from random import randint
            deltax = randint(0, 960)
            deltay = randint(0, 540)

            msg = "{} {}".format(deltax, deltay)
            self.sock.sendto(msg, (self.UdpIp, self.UdpPort))
            i = i + 1
            """
            msg = {"cord1": rand.random() * 0.3, "cord2": rand.random() *0.3}
            send_msg = json.dumps(msg).encode('utf-8')
            self.sock.sendto(send_msg, (self.UdpIp, self.UdpPort))
            """
            """
            cord =  [13.4, 12.4, 10.4, 14.4]
            msg = array(cord)

            self.sock.sendto(msg, (self.UdpIp, self.UdpPort))
            """


    def server(self):
        self.sock.bind((self.UdpIp, self.UdpServerPort))
        log.info("Waiting on receive")

        while True:
            data, addr =  self.sock.recvfrom(1024)
            log.info('Received {} Bytes. Msg: {} addr {}'.format(len(data), data, addr))

            try:

                """
                c = data.decode("utf-8")
                data_dict = json.loads(c)
                log.info('data dict is {}'.format(data_dict["cord1"]))
                """
                import pickle
                try:
                    d = pickle.loads(data)
                    log.info('Data recv is %s', d)
                    log.info('data[0] {} data[1] {}'.format(d[0], d[1]))
                except Exception as e:
                    log.exception(e)


            except Exception as e:
                log.exception(e)
                log.error("Exception on reading the dict")
                sys.exit(0)


def help():
    log.info('Need either client or server argument: syntax: udp.py c/client or udp.py s/server')

def main(argv):
    server = False
    client = False
    try:
        opts, args = getopt.getopt(argv, 'hcs', ["client", "server"])
    except Exception as e:
        log.info('Exception reading arguments {}'.format(e.message))

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            help()
            sys.exit(0)

        elif opt == '-s' or opt == '--server':
            server = True
        elif opt == '-c' or opt == '--client':
            client = True

    if client and server:
        help()
        sys.exit(0)

    if not client and not server:
        help()
        sys.exit(0)

    conn = UdpClientServer()

    if client:
        conn.client()

    if server:
        conn.server()


if __name__ == '__main__':
    main(sys.argv[1:])
