#TODO: Ask the user to enter a username 
username = input("Enter your first intial and last name with no spaces: \n")

#TODO: Ask the user to enter the device name 
device_name = input("Your device name will be the device type paired with the month and day you were born (written in mm/dd format with no spaces.)\n")
#TODO: Ask the user to enter a temporary password 
temporary_password = input("Your temporary password will be your first intial, the first 3 letters of your last name and the year you were born written in YYYY format with no spaces. \n")

#Clean the Input 
#this will get rid of the spaces at the beginning and end
cleaned_username = username.strip(" ")
cleaned_device_name = device_name.strip(" ")
cleaned_password = temporary_password.strip(" ")


#Process the string data: 

#TODO: Display the first four characters of the device name
print(f"Device Name: {cleaned_device_name[0:4]}")

#TODO: Determine whether the password is less than eight characters
if len(cleaned_password) > 8: 
    print("Password is too long")


#TODO: Display a formatted summary report for the IT Technician

print(f"Username: {cleaned_username}")
print(f"Device Name: {cleaned_device_name}")
print(f"Temporary Password: {cleaned_password}")