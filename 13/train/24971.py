from ipaddress import ip_network

net = ip_network('111.222.0.124/255.255.224.0', 0)

for ip in list(net)[::-1]:
    ip_bin = f'{int(ip):032b}'
    if (ip_bin.count('1') * ip_bin.count('0') % 2):
        print(sum(map(int, str(ip).split('.'))))
        break
