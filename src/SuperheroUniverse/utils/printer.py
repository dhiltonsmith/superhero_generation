class SingletonPrinter():
    class __SingletonPrinter:
        def __init__(self, arg):
            self.val = arg

        def invalid_choice(self):
            print "Invalid Option"

        def print_menu(self, options):
            menu = {}
            for option in options:
                menu[len(menu)+1] = option

            for key in sorted(menu.keys()):
                print "%s: %s" % (key, menu[key][0])

            try:
                response = int(raw_input("Selection: "))
            except ValueError:
                return self.print_menu(options)
            if response > 0 and response < len(menu) + 1:
                return menu[response][1]()
            else:
                self.invalid_choice()
                return self.print_menu(options)

    instance = None
    def __init__(self, arg):
        if not SingletonPrinter.instance:
            SingletonPrinter.instance = SingletonPrinter.__SingletonPrinter(arg)
        else:
            SingletonPrinter.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
