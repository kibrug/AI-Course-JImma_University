import ipaddress


def hostNattworkingip4():

    try:
        ip = ipaddress.ip_address("192.0.2.1")
        print(ipaddress.ip_address('192.8.2.1'))

        print(ip)
    except:
        print("Exeption Occures")


hostNattworkingip4()



def ipnatworkinIP6():
    n=ipaddress.ip_address(42540766411282592856903984951653826561)
    k = ipaddress.ip_address(42540766411282592856903984951653826000)
    try:
        print(f"Ip of n {n}")
        print(f"Ip of k {k}")
    except:
        print("Exption Happend")
ipnatworkinIP6()


