from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.114',
    'username': 'admin',
    'password': '0000',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar_router1 = [
    '/ip address add address=172.26.22.1/25 interface=eth3',
    '/ip address add address=192.168.22.1/30 interface=eth2',
    '/ip address add address=dhcp interface=eth1',
    '/ip firewall nat add chain=srcnat out-interface=eth1 action=masquerade',
    '/ip pool add name=dhcp_pool1 ranges=172.26.22.2-172.26.22.126',
    '/ip dhcp-server add address-pool=dhcp_pool1 interface=eth3 name=dhcp1',
    '/ip dhcp-server network add address=172.26.22.0/25 gateway=172.26.22.1',
    '/ip service enable ssh',
    '/ip route add dst-address=172.26.22.128/25 gateway=192.168.22.1',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar_router1)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()