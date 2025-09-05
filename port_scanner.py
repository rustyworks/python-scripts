import argparse
import socket


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname")
    parser.add_argument("--timeout", type=float, default=1)
    args = parser.parse_args()
    hostname = args.hostname
    timeout = args.timeout
    ip = socket.gethostbyname(hostname)
    for port in range(1, 65536):
        s = socket.socket()
        s.settimeout(timeout)
        result = s.connect_ex((ip, port))
        if result == 0:
            port_name = ""
            try:
                port_name = socket.getservbyport(port, "tcp")
            except OSError:
                pass
            print(f"port {port_name} {port} opened")
        s.close()


if __name__ == "__main__":
    main()
