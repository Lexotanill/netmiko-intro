from netmiko import ConnectHandler

router_mikrotik = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.70',
    'username': 'admin',
    'password': '0000',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

conexion = ConnectHandler(**router_mikrotik)

# Definir comandos a ejecutar
configurar = [
    '/ip pool add name=dhcp_pool ranges=172.25.22.129-172.25.22.254',
    '/ip dhcp-server add address-pool=dhcp_pool interface=ether3 name=dhcp1',
    '/port set 0 name=serial0 ',
    '/port set 1 name=serial1',
    '/ip address add address=172.25.22.1/25 interface=ether2 network=172.25.22.0',
    '/ip dhcp-client add interface=ether1',
    '/ip dhcp-server network add address=172.25.22.128/25 dns-server=8.8.8.8 gateway=172.25.22.129',
    '/ip dns set servers=8.8.8.8,8.8.4.4',
    '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
]

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()