import sys
import argparse

from SuperheroUniverse.utils.printer import SingletonPrinter

def arg_parse():
    parser = argparse.ArgumentParser(description='Start your Universe')

    return parser.parse_args()

def start_universe():
    return 1

def break_out():
    return 0

def start_menu():
    continue_flag = 1
    while continue_flag:
        menu = [("Start Universe", start_universe),
            ("Exit", break_out)]
        continue_flag = printer.print_menu(menu)

def main():
    global args, printer
    args = arg_parse()
    printer = SingletonPrinter("Printer")
    start_menu()

if __name__ == "__main__":
    main()

