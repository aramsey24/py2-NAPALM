import json
from napalm import get_network_driver

bgplist = ['192.168.122.27',
           '192.168.122.28',
           '192.168.122.29'
           ]
        
for ip_address in bgplist:
    print('connecting to ' + str(ip_address))
    driver = get_network_driver('ios')
    bgp_routers = driver(ip_address, 'cisco', 'cisco')
    bgp_routers.open()
    bgp_neighbors = bgp_routers.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    bgp_routers.close()
