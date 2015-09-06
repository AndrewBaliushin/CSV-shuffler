import unittest

from csv_shufler import HelpPrinter


class TestSimple(unittest.TestCase):

    def print_help_test(self):
        print("printing help")
        HelpPrinter.print_help()