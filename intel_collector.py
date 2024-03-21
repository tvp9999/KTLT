import socket


def get_server_info(target):
    try:
        ip_addr = socket.gethostbyname(target)
        hostname, _, _ = socket.gethostbyaddr(ip_addr)
        return hostname, ip_addr
    except socket.gaierror as e:
        print(f'Error: {e}')
        return None, None


def port_scan(addr, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        res = s.connect_ex((addr, port))

        if res == 0:
            print(f'{port} : open')
        else:
            print(f'{port} : close')
        s.close()
    except socket.error as e:
        print(f'Error: {e}')


def main():
    try:
        target = input('Enter target: ')
        ports = [21, 22, 23, 53, 80, 443, 8080]

        print('SERVER INFORMATION')
        hostname, ip_addr = get_server_info(target)

        if hostname is not None and ip_addr is not None:
            print(f'Hostname: {hostname}')
            print(f'IP: {ip_addr}')


        print('Scanning...')
        for port in ports:
            port_scan(target, port)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()