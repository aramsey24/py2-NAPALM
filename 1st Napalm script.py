#json makes the output of scripts from napalam i.e "get_facts" easier to read. 
#napalm allows for retrieving configuration and state of devices in addition to making changes
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios_switch = driver('192.168.122.26', 'cisco', 'cisco')

#SSH to the switch using below command
ios_switch.open()

#one of the functions available in NAPALM IS "get_facts" -https://napalm.readthedocs.io/en/latest/validate/index.html?highlight=get_facts
ios_output = ios_switch.get_facts()
print (json.dumps(ios_output, sort_keys=True, indent=4))


ios_output = ios_switch.get_interfaces()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = ios_switch.get_interfaces_counters()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = ios_switch.get_interfaces_ip()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = ios_switch.get_mac_address_table()
print (json.dumps(ios_output, sort_keys=True, indent=4))
