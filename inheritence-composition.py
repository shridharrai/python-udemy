class BaseChai:
    def __init__(self, type_):
        self.type = type_
    
    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):  # Inheritence
    def add_spices(self):
        print(f"Adding Spices for {self.type}")

class ChaiShop:
    base_chai = BaseChai  # Composition

    def __init__(self):
        self.chai = self.base_chai("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} in shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    base_chai = MasalaChai # override the base_chai attr of ChaiShop
        
shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()