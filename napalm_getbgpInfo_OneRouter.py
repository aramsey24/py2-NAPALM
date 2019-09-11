#json makes the output of scripts from napalam i.e "get_facts" easier to read. 


import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios_switch = driver('192.168.122.27', 'cisco', 'cisco')
ios_switch.open()



bgp_neighbors = ios_switch.get_bgp_neighbors()
print(json.dumps(bgp_neighbors, indent=4))

ios_switch.close()
     
