# Task is to create a Python script responsible for keeping track of company devices and their assigned users 

#TODO: Track available devices 
devices = ["Iphone 14", "MacBook Pro", "Ipad 10th Gen", "Iphone 16 Pro", "HP Pavillion", "Chromebook"]
print("Available Devices:\n", devices)
print("Total Devices", len(devices))
#TODO: Assign devices to users 
assigned_devices = {"MScott": "Iphone 14", "RBlack": "Ipad 10th Gen", "JSmart": "Chromebook"}
print("Assigned Devices:\n", assigned_devices)

#TODO: Update Inventory and Assignments
devices.append("Ipad Pro")
print("Updated Inventory:\n", devices)
assigned_devices.update({"MScott": "Iphone 16 Pro"})
print("Updated Assignments:\n", assigned_devices)

#TODO: Display a summary
print("IT Asset Summary:")
print("Total Devices", (len(devices)))
print("Assigned Devices:\n", assigned_devices)
      
