class HelpPrinter():
    """Print help file"""
    helpFileName = "data/README.md"

    @staticmethod
    def print_help():
        f = open(HelpPrinter.helpFileName, "r")
        print(f.read())

