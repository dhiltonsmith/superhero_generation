from SuperheroUniverse.utils.printer import SingletonPrinter

class Side():
    def __init__(self):
        self.printer = SingletonPrinter("Printer")
        self.create_side()

    def create_side(self):
        self.name = self.printer.print_string_question("What is the name of this side? ")
