import socket
import time
def get_server_info(target):
    try:
        ip_addr = socket.gethostbyname(target)
        hostname, _, _ = socket.gethostbyaddr(ip_addr)
        return hostname, ip_addr
    except socket.gaierror as e:
        print(f'Error: {e}')
        return None, None

def scan(target_host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"[*] Port {port}")
    except socket.timeout:
        print(f"[-] Port {port}closed (Timeout)")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def port_scan(target_host, ports):
    print(f"Scanning target: {target_host}")
    start_time = time.time()
    for port in ports:
        scan(target_host, port)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    try:
        target_host = input("Enter target: ")

        print('SERVER INFORMATION')
        hostname, ip_addr = get_server_info(target_host)

        if hostname and ip_addr:
            print(f'Hostname: {hostname}')
            print(f'IP: {ip_addr}')

        ports = [21, 22, 23, 80, 443, 3306, 8080]
        port_scan(target_host, ports)
    except Exception as e:
        print(f'Error: {e}')
