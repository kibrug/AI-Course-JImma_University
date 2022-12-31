# Networking by useing ip_neworking

import ipaddress

def networking():

    ip4=ipaddress.ip_network('192.0.2.0/24')
    ip6 =ipaddress.ip_network('2001:db8::0/96')
    try:
        print(f" Networking of {ip4}")
        print(f" Networking of {ip6}")
    except:
        print("Exetiption happen")
networking()

