import sys, inspect
from HelpPrinter import HelpPrinter
from CsvParser import CsvParser
from shuffling_strategies.SameDataRandomChoice import SameDataRandomChoice

shuffling_stratagies_for_columns = {0: SameDataRandomChoice(), 1: SameDataRandomChoice(), 2: SameDataRandomChoice()}

def main():
    """Entry point for the application script"""
    if len(sys.argv) != 1:
        csv_parser = CsvParser(path_to_csv=sys.argv[1], delimiter=';')
       

    else:
        HelpPrinter.print_help()


if __name__ == "__main__":
    main();

