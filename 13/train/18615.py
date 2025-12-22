from ipaddress import ip_network

for mask in range(32, -1, -1):
    net = ip_network(f'143.131.211.37/{mask}', False)
    c_ones = 0

    for ip in net:
        c_ones += 1 if f'{int(ip):032b}'.count('1') == 10 else 0
        if c_ones > 15:
            break

    if c_ones == 15:
        print(mask)
        break
