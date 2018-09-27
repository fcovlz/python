"""
@ Description
    Brief example of how inheritance works

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        inheritance_example.py
"""


class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chases_cats(self):
        return self.chases_cats


class Cat(Pet): 
    def __init__(self, name, hates_dogs):
        Pet.__init__(self, name, "Cat") 
        self.hates_dogs = hates_dogs

    def hates_dogs(self):
        return self.hates_dogs


class Hater(Cat, Dog):
    def __init__(self, name, hates):
        Dog.__init__(self, name, "Dog")
        Cat.__init__(self, name, "Cat")
        self.chases_hates = hates
        
    def hates(self): 
        return self.chases_hates


if __name__ == "__main__":
    hater = Hater(name="hater", hates=True)
    doggy = Dog(name="doggy", chases_cats=True)
    catty = Cat(name="catty", hates_dogs=True)
