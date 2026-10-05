import socket
import time

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    return open_ports

def main():
    print("Starting port scan...")
    ip = "127.0.0.1"  # Change this to the target IP address
    ports = range(1, 1025)  # Common ports to scan
    open_ports = scan_ports(ip, ports)
    print(f"Open ports: {open_ports}")
    print("Scan completed.")

if __name__ == "__main__":
    main()
