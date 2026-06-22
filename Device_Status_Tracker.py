#TODO: Store device data using a dictionary {device name: status}

devices = {
    "Router": "Online",
    "Printer1": "Offline", 
    "Server2": "Online",
    "Switch": "Online",
    "Printer5": "Online", 
    "Server4": "Offline",
    "Server10": "Online"
}
#TODO: Use a function to check device status and print a message
#TODO: Conditional logic offline = flag it, online = confirm normal ops
#TODO: Use a loop to check each device in the dictionary
#TODO: Produce  clear message readable by the IT staff

def check_device_status():
    print("Checking device status...")
    for device in devices:
        status = devices[device]
        if status == "Offline":
            print(f"{device} is OFFLINE. Action required.")
        elif status == "Online":
            print(f"{device} is ONLINE and operating normally.")
    else:
        print("Status check complete.")

check_device_status()

devices["Backup Router"] = "Offline"
check_device_status()

