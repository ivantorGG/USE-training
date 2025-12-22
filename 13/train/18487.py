from ipaddress import ip_network

for A in range(256):
    net = ip_network(f'192.214.{A}.184/255.255.255.224', False)

    count_ones = 0
    for ip in net:
        if f'{int(ip):032b}'.count('1') <= 15:
            break
    else:
        print(A)
        break
