# jun/28/2024 14:11:50 by RouterOS 7.6
# software id = 
#
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/ip pool
add name=dhcp_pool ranges=172.25.22.129-172.25.22.254
/ip dhcp-server
add address-pool=dhcp_pool interface=ether3 name=dhcp1
/port
set 0 name=serial0
set 1 name=serial1
/ip address
add address=172.25.22.1/25 interface=ether2 network=172.25.22.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server network
add address=172.25.22.128/25 dns-server=8.8.8.8 gateway=172.25.22.129
/ip dns
set servers=8.8.8.8,8.8.4.4
/ip firewall nat
add action=masquerade chain=srcnat out-interface=ether1
