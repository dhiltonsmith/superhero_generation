from SuperheroUniverse.utils.printer import SingletonPrinter

class Universe():
    def __init__(self, name):
        self.name = name
        self.printer = SingletonPrinter("Printer")

    def break_out(self):
        return 0    

    def rename_universe(self):
        name = self.printer.print_string_question("What is the new name of your universe? ")
        self.name = name
        return 1

    def universe_menu(self):
        continue_flag = 1
        while continue_flag:
            header = "%s Universe Menu" % self.name
            menu = []
            menu.append(("Rename %s Universe" % self.name, self.rename_universe))
            menu.append(("Back", self.break_out))
            continue_flag = self.printer.print_menu(header, menu)
        return 1
