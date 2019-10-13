from SuperheroUniverse.side import Side
from SuperheroUniverse.utils.printer import SingletonPrinter

class Faction():
    sides = []

    def __init__(self):
        self.printer = SingletonPrinter("Printer")
        self.create_faction()

    def create_faction(self):
        self.name = self.printer.print_string_question("What is the name of your faction? ")
        self.sides_count = self.printer.print_integer_question("How many sides exist within this faction (Minimum: 2)? ", 2)
        for side in range(self.sides_count):
            self.sides.append(Side())
