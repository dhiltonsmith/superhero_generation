class SingletonPrinter():
    class __SingletonPrinter:
        def __init__(self, printer_name = "Printer"):
            self.printer_name = printer_name

        def invalid_choice(self):
            print "Invalid Option"

        def print_menu(self, header, options):
            print "\n---- %s ----\n" % (header)
            menu = {}
            for option in options:
                menu[len(menu)+1] = option

            for key in sorted(menu.keys()):
                print "%s: %s" % (key, menu[key][0])

            try:
                response = int(raw_input("Selection: "))
            except ValueError:
                self.invalid_choice()
                return self.print_menu(header, options)
            if response > 0 and response < len(menu) + 1:
                return menu[response][1]()
            else:
                self.invalid_choice()
                return self.print_menu(header, options)

        def print_string_question(self, question):
            return raw_input(question)

    instance = None
    def __init__(self, arg):
        if not SingletonPrinter.instance:
            SingletonPrinter.instance = SingletonPrinter.__SingletonPrinter(arg)
    def __getattr__(self, name):
        return getattr(self.instance, name)
