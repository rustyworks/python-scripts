import socket
import threading
import sys


def usage():
    print("Usage: python client.py <username> <channel>")


def channel(channel):
    if not channel.startswith('#'):
        return f"#{channel}"
    return channel


def print_response(client):
    resp = client.get_response()
    print(resp)
    if resp:
        msg = resp.strip().split(':')
        print(f"< {msg[1].split('!')[0]}> {msg[2].strip()}")


class IRCSimpleClient:

    def __init__(self, username, channel, server='irc.libera.chat', port=6667):
        self.username = username
        self.server = server
        self.port = port
        self.channel = channel

    def connect(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.server, self.port))

    def get_response(self):
        return self.conn.recv(512).decode('utf-8')

    def send_cmd(self, cmd, message):
        command = f"{cmd} {message}\n".encode('utf-8')
        self.conn.send(command)

    def send_message_to_channel(self, message):
        command = f"PRIVMSG {self.channel}"
        message = f":{message}"
        self.send_cmd(command, message)

    def join_channel(self):
        cmd = "JOIN"
        channel = self.channel
        self.send_cmd(cmd, channel)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        exit(0)
    else:
        username = sys.argv[1]
        channel = channel(sys.argv[2])

    cmd = ""
    joined = False
    client = IRCSimpleClient(username, channel)
    client.connect()

    while not joined:
        resp = client.get_response()
        print(resp.strip())
        if "No Ident response" in resp:
            client.send_cmd("NICK", username)
            client.send_cmd(
                "USER", f"{username} * * :{username}"
            )

        if "376" in resp:
            client.join_channel()

        if "433" in resp:
            username = "_" + username
            client.send_cmd("NICK", username)
            client.send_cmd(
                "USER", f"{username} * * :{username}"
            )

        if "PING" in resp:
            client.send_cmd("PONG", ":" + resp.split(":")[1])

        if "366" in resp:
            joined = True

    while cmd != "/quit":
        cmd = input(f"< {username}>").strip()
        if cmd == "/quit":
            client.send_cmd("QUIT", "Good bye!")
        client.send_message_to_channel(cmd)

        response_thread = threading.Thread(
            target=print_response,
            args=(client,)
        )
        response_thread.daemon = True
        response_thread.start()
