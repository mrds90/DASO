# class that Read CSV file and parse it to JSON
import sys


class ParserService:
    def __init__(self, file_name):
        self.file_name = file_name

    def parse_csv_to_json(self):
        import csv
        import json
        with open(self.file_name, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
            json_data = json.dumps(data)
            return json_data

# class that Send JSON by socket UDP


class SocketService:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_json_by_udp(self, json_data):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(json_data.encode(), (self.host, self.port))


# app that create UDP client and send JSON data every 30 seconds
class App:
    def __init__(self, host, port, file_name):
        self.host = host
        self.port = port
        self.file_name = file_name

    def run(self):
        import time
        import json
        import sys
        import os
        import csv
        import socket
        import threading
        import datetime
        import random
        import string

        # create UDP client
        udp_client = SocketService(self.host, self.port)

        # create ParserService object
        parser_service = ParserService(self.file_name)

        # create JSON data
        json_data = parser_service.parse_csv_to_json()

        # send JSON data by UDP
        udp_client.send_json_by_udp(json_data)

        # create thread that send JSON data every 30 seconds
        threading.Timer(30, self.run).start()


# import sys argument
if __name__ == "__main__":
    # (localhost, 10000, "data.csv")
    app = App(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    app.run()
