zoo = ("tiger", "orangutan", "giraffe", "rhino",
       "lion", "snow leopard", "red panda", "otter", "flamingo", "fox")

print(zoo.index("snow leopard"))

animal_exists = "hippo"

if animal_exists in zoo:
    print(f"A {animal_exists} exists!")
else:
    print(f"No {animal_exists} was found.")

wild_things = list(zoo)
wild_things.extend(["honey badger", "king cobra", "walrus"])
wild_things = tuple(wild_things)
print(wild_things)
