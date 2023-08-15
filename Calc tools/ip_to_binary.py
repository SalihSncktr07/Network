import ipaddress

def ip_to_binary(ip):
    ip_obj = ipaddress.ip_address(ip)
    binary_octets = []
    
    for octet in ip_obj.packed:
        binary_octets.append(bin(octet)[2:].zfill(8))
    
    binary_ip = '.'.join(binary_octets)
    return binary_ip

ip_address = input("IP Adresini giriniz: ")

binary_ip = ip_to_binary(ip_address)
print(f"IP Adresi Binary: {binary_ip}")

while True:
    pass