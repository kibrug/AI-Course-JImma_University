import ipaddress

# Host Interface

def hostIntterFace():

    hi4 = ipaddress.ip_interface('192.0.2.1/24')
    hi6 = ipaddress.ip_interface('2001:db8::1/96')
    try:
        print(f"Ip for Intreface of {hi4}")
        print(f"Ip of Interface of ip6 {hi6}")
    except:
        print("Exption Happend")

hostIntterFace()
