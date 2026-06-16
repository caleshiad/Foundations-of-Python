# Dicitonary storing server configuration details 
server_config = {
    "hostname": "web-server-01",
    "ip_address": "192.168.1.10",
    "operating_system": "Linux",
    "status": "online",
}

# Access a specific configuration value 
print("Server IP Address:", server_config["ip_address"])

# Display all configuration keys
print("Configuration keys:", server_config.keys())

# Display all configuration values 
print("Configuration values:", server_config.values())

# Display all configuration key-value pairs
print("Configuration items:", server_config.items())