# Diccionarios

phonebook = {
    "mich" : 3310249922,
    "jake" : 3318263823,
    "rudy" : 3321223323,
    "Jill" : 947662781
}

# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

phonebook["Jake"] = 9382734343
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
    
# Iterating over dictionaries

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name,number))
    
# Removing a value

del phonebook["mich"]

phonebook.pop("rudy")