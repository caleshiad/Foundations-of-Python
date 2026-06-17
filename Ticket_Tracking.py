
tickets = {
    "Ticket 1001": "high" ,
    "Ticket 1002": "high",
    "Ticket 1003": "low",
    "Ticket 1004": "medium",
    "Ticket 1005": "medium",
    "Ticket 1006":  "low",
    "Ticket 1007": "low",
    "Ticket 1008": "high",
    "Ticket 1009": "medium",
    "Ticket 1010": "high",
    "Ticket 1011": "medium",
    "Ticket 1012": "low",
    "Ticket 1013": "high",
    "Ticket 1014": "low",
    "Ticket 1015": "medium"
    }

for ticket in tickets:
    priority = tickets[ticket]
# for ticket, priority in tickets.items() --- another way to write the preceding 2 lines of code
    if  priority == "high":
        print("High Priority ticket- immediate action required")
    elif  priority == "medium":
        print("Medium Priority ticket- schedule for today")
    elif  priority == "low":
        print("Low priority ticket- add to backlog") 
    

for ticket in tickets:
    print("Resolving ticket...")
print("All tickets have been resolved.")