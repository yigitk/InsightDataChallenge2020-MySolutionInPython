import unittest
import os
import csv
from IO.PopulationChangeSummaryWriter import PopulationChangeSummaryWriter
from IO.TractPopulationChangeReader import TractPopulationChangeReader
from Entities.AreaPopulationChangeSummary import AreaPopulationChangeSummary
from Processing.TractPopulationChangeSummarizer import TractPopulationChangeSummarizer
from Processing.TractPopulationChangeProccessor import TractPopulationChangeProccessor
import constants as CONSTANTS

dummy_file_path = "../input/dummy.csv"

class TestStringMethods(unittest.TestCase):
    '''Test to check the basic line behavior'''
    def test_basic_line_processing(self):
        reader = TractPopulationChangeReader()
        proccessor = TractPopulationChangeProccessor()
        fake_file_lines = ["1005950100,01,005,950100,187.3614167,11.21928403,,21640,\"Eufaula, AL - GA\",,2,C,3848,1735,3321,1627,-527,-13.70,-108,-6.22"]
        lines = [l for l in csv.reader(fake_file_lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)]
        parsed_columns = reader.check_collumns(lines[0])
        proccessor.parse_text_to_datum(parsed_columns)
        
    '''Test to check the basic line behavior when there is an invalid column in data'''
    def test_line_processing_invalid_data_test(self):
        reader = TractPopulationChangeReader("../input/InvalidColumnValueData.csv")
        reader.open_and_validate_file()
        proccessor = TractPopulationChangeProccessor()
        with self.assertRaises(ArithmeticError):
            while True:
                reader.readLine(proccessor.parse_text_to_datum)
                
    '''Test to check some of the numbers in quotes which are corner cases'''
    def test_Line_processing_with_quoted_values_test(self):
        reader = TractPopulationChangeReader()
        proccessor = TractPopulationChangeProccessor()
        fake_file_lines = ["02185000300,02,185,000300,3171.90115,849.3578553,,,,,3,,8,2,2527,1,2519,\"31,487.50\",-1,-50.00"]
        lines = [l for l in csv.reader(fake_file_lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)]
        parsed_columns = reader.check_collumns(lines[0])
        proccessor.parse_text_to_datum(parsed_columns)


if __name__ == '__main__':
    unittest.main()
