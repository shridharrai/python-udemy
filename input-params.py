def make_chai(tea, sugar):
    print(f"Tea: {tea}, Sugar: {sugar}")

make_chai("Cinnamon", "low") # positional params
make_chai(sugar = "medium", tea = "Cardamom") # keywords params

def special_chai(*ingreds, **extras): # * -> args, ** -> keyword args
    print(f"Ingreds: {ingreds}, Extras: {extras}")

special_chai("Cinnamon", "Cardamom", sugar = "low", milk = "no")