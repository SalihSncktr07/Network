import ipaddress

def calculate_ip_count(ip, subnet_mask):
    ip_obj = ipaddress.ip_interface(f"{ip}/{subnet_mask}")
    network = ip_obj.network
    ip_count = network.num_addresses
    return ip_count

ip_address = input("IP Adresini giriniz: ")
subnet_mask = input("Subnet Mask giriniz: ")

ip_count = calculate_ip_count(ip_address, subnet_mask)
print(f"Verilen IP Adresi ve Alt Ağ Maskesi ile Alınabilecek IP Adresi Sayısı: {ip_count}")

while True:
    pass