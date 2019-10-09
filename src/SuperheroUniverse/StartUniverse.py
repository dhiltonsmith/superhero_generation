import sys
import argparse

from SuperheroUniverse.universe import Universe
from SuperheroUniverse.utils.printer import SingletonPrinter

universe = None

def arg_parse():
    parser = argparse.ArgumentParser(description='Start your Universe')

    return parser.parse_args()

def start_universe():
    global universe
    name = printer.print_string_question("What is the name of your universe? ")
    universe = Universe(name)
    return 1

def break_out():
    return 0

def start_menu():
    continue_flag = 1
    while continue_flag:
        header = "Main Menu"
        menu = []
        if universe == None:
            menu.append(("Start Universe", start_universe))
        else:
            menu.append(("Restart Universe", start_universe))
        if universe != None:
            menu.append(("Explore %s Universe" % (universe.name), universe.universe_menu))
        menu.append(("Exit", break_out))
        continue_flag = printer.print_menu(header, menu)

def main():
    global args, printer
    args = arg_parse()
    printer = SingletonPrinter("Printer")
    start_menu()

if __name__ == "__main__":
    main()

