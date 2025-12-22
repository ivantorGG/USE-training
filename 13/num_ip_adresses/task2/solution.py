# https://www.youtube.com/watch?v=DBoXMHFFPc4&t=795s

from ipaddress import ip_network

c = 0
net = ip_network('202.75.38.152/255.255.255.248', False)

for ip in net:
    ip_bin = f'{int(ip):032b}'
    if '111' in ip_bin:
        c += 1

print(c)

# 4
