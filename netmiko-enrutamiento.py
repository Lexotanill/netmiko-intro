from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   'ip',
    'username': 'admin',
    'password': '0000',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar_router1 = [
    '/ip address add address=172.26.22.1/25 interface=eth3',
    '/ip address add address=192.168.1.1/30 interface=eth2',
    '/ip address add address=dhcp interface=eth1',

    '/ip firewall nat add chain=srcnat out-interface=eth1 action=masquerade',

    '/ip pool add name=dhcp_pool1 ranges=172.26.22.2-172.26.22.126',
    '/ip dhcp-server add address-pool=dhcp_pool1 interface=eth3 name=dhcp1',
    '/ip dhcp-server network add address=172.26.22.0/25 gateway=172.26.22.1',

    '/ip service enable ssh',

    '/ip route add dst-address=172.26.22.128/25 gateway=192.168.1.2',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar_router1)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

from netmiko import ConnectHandler

router_cisco = {
    'device_type': 'cisco_ios',
    'host':   '10.0.0.56',
    'username': 'admin',
    'password': 'admin',
    'port': 22,            # optional, defaults to 22
    'secret': '',          # optional, defaults to ''
}

conexion = ConnectHandler(**router_cisco)

# Definir comandos a ejecutar
# Definir comandos a ejecutar para Router 2 (Cisco)
configurar_router2 = [
    # Asignar IPs a las interfaces
    'interface e0/0',
    'ip address 172.26.22.129 255.255.255.128',
    'no shutdown',

    'interface e0/1',
    'ip address 192.168.1.2 255.255.255.252',
    'no shutdown',

    'interface e0/2',
    'ip address dhcp',
    'no shutdown',

    # Habilitar NAT
    'access-list 1 permit 172.26.22.128 0.0.0.127',
    'ip nat inside source list 1 interface e0/2 overload',
    'interface e0/0',
    'ip nat inside',
    'interface e0/1',
    'ip nat inside',
    'interface e0/2',
    'ip nat outside',

    # Configurar DHCP Server
    'ip dhcp pool DHCP_POOL2',
    'network 172.26.22.128 255.255.255.128',
    'default-router 172.26.22.129',

    # Habilitar SSH
    'hostname Router2',
    'ip ssh version 2',
    'crypto key generate rsa modulus 1024',
    'username admin privilege 15 secret 0000',
    'line vty 0 4',
    'transport input ssh',
    'login local',

    # Configurar el enrutamiento estático hacia Router 1
    'ip route 172.26.22.0 255.255.255.128 192.168.1.1',
]


# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar_router2 )
print(accion1)

# Cerrar la conexión
conexion.disconnect()