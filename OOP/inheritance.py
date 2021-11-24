class GrandParent:
    """Demonstrating the concept of inheritance."""

    def __init__(self, name, clan):
        self.name = name
        self.clan = clan

    def parent_method(self):
        print(f'I am the Grand Parent and my name is: {self.name} !')
        print(f'My clan is {self.clan}')


class Parent(GrandParent):
    """This class inherits from the GrandParent class"""

    def __init__(self, name, clan, other_name):
        super().__init__(name, clan)
        self.other_name = other_name

    # Override the parent method
    def parent_method(self):
        print(f'My full name is {self.other_name} {self.name} and I am a child of {self.name}')


grandpa = GrandParent("Juma", "Khayo")
grandpa.parent_method()

parent = Parent("Lutere", "Wanga", "Mumia")
parent.parent_method()
