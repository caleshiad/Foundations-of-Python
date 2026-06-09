#TODO: prompts the user to enter server uptime in days
uptime = int(input("Enter server uptime in days:"))

#TODO: converts uptime to hours
uptime_hours = uptime * 24

#TODO: prompts the user to enter the current number of active users
active_users = int(input("Enter current number of active users:"))

#TODO: adds 1 to represent a new user log-in
active_users +=1

#TODO: prompts the user to enter total disk space (GB) and used disk #space (GB)
total_disk_space = int(input ("Enter total disk space (GB):"))
used_disk_space = int(input ("Enter used disk space (GB):"))

#TODO: calculates available disk space
available_disk_space = total_disk_space - used_disk_space

#TODO: prints a clear status report with results

#print uptime 
print(f"Uptime: {uptime} days")
print(f"Uptime: {uptime_hours} hours")

#print active users 
print(f"Active Users: {active_users}")

#print total disk space
print(f"Total Disk Space: {total_disk_space} GB")

#print used disk space
print(f"Used Disk Space: {used_disk_space} GB")

#print available disk space
print(f"Available Disk Space: {available_disk_space} GB")