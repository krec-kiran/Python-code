import random


class PetShop():

    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.  We can set it at will."""

        self.pet_factory = animal_factory
        print(animal_factory)

    def show_pet(self):
        """Creates and shows a pet using the abstract factory"""
        print(self.pet_factory())
        pet = self.pet_factory()
        # pet = Dog()
        print("We have a lovely {}".format(pet))
        print("It says {}".format(pet.speak()))


class Dog():
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat():
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"


# Additional factories:

# Create a random animal
def random_animal():
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])()


# Show pets with various factories
if __name__ == "__main__":

    # A Shop that sells only cats
    cat_shop = PetShop(Dog)
    cat_shop.show_pet()
    print("")

    # A shop that sells random animals
    # shop = PetShop(random_animal)
    # for i in range(3):
    #     shop.show_pet()
    #     print("=" * 20)
