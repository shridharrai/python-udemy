chai_types = ["light", "kadak", "kadak"]

flitered_chai = list(filter(lambda chai : chai != 'kadak', chai_types))

print(flitered_chai)