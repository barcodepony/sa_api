from multiprocessing.connection import Client
import time
class QueueClient(object):
    def __init__(self, address: str = "0.0.0.0", port: int = 6000, authkey=b'defaultkey'):
        self.address = address
        self.port = port
        self.__key = authkey
        self.client = None
        while self.client is None:
            try:
                self.client = Client((self.address, self.port), authkey=self.__key)
            except ConnectionRefusedError as e:
                print("Error: %s" % e)
                print("Retrying in 2.5s")
                self.client = None
                time.sleep(2.5)

    def send(self, sql: str):
        print("SENDING: %s" % sql)
        self.client.send(sql)
