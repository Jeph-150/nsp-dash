# Import modules
import os
import ipaddress

# My subnet
network = ipaddress.ip_network("172.21.18.0/24", strict=False)

# Loop through out the whole subnet while sending package to each IP's
for ip in network.hosts():  # .hosts() skips .0 and .255
    response = os.system(f"ping -n 1 -w 100 {ip}")  # send 1 ping packet and wait for 100 ms
    if response == 0:
        print(f"{ip} is up!")
    else:
       print(f"{ip} is down.")
