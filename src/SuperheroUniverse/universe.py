from SuperheroUniverse.faction import Faction
from SuperheroUniverse.utils.printer import SingletonPrinter

class Universe():
    factions = []

    def __init__(self, name):
        self.name = name
        self.printer = SingletonPrinter("Printer")

    def break_out(self):
        return 0    

    def faction_create(self):
        current_faction = Faction()
        self.factions.append(current_faction)
        return 1

    def faction_menu(self):
        continue_flag = 1
        while continue_flag:
            header = "%s Universe Menu - Factions" % self.name
            menu = []
            menu.append(("Create New Faction", self.faction_create))
            if len(self.factions) > 0:
                menu.append(("Print Factions", self.factions_print))
            menu.append(("Back", self.break_out))
            continue_flag = self.printer.print_menu(header, menu)
        return 1

    def factions_print(self):
        print self.factions
        return 1

    def rename_universe(self):
        self.name = self.printer.print_string_question("What is the new name of your universe? ")
        return 1

    def universe_menu(self):
        continue_flag = 1
        while continue_flag:
            header = "%s Universe Menu" % self.name
            menu = []
            menu.append(("Rename %s Universe" % self.name, self.rename_universe))
            menu.append(("Factions in %s Universe" % self.name, self.faction_menu))
            menu.append(("Back", self.break_out))
            continue_flag = self.printer.print_menu(header, menu)
        return 1
