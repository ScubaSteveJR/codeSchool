import csv

with open("phonebook.csv", "a") as file:

    name = input("Name: ")
    number = input("Number: ")
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})


##people = {  ## or dict()
##    "Carter": "+1-225-456-8743",
##    "Stephen": "+1-337-456-1221"
##}

##name = input("Name: ")
##if name in people:
##    number = people[name]
##    print(f"Number: {number}")