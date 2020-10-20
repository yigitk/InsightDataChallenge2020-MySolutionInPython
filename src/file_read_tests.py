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
    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            TractPopulationChangeReader(dummy_file_path)

    
    def test_open_file(self):
        TractPopulationChangeReader()
    
    def test_open_invalid_file(self):
        with self.assertRaises(Exception):
            TractPopulationChangeReader("../input/censustract-00-10.xlsx").open_and_validate_file()
    
    def test_parse_line(self):        
        test_line = ["01005950100,01,005,950100,187.3614167,11.21928403,,21640,\"Eufaula, AL - GA\",,2,C,3848,1735,3321,1627,-527,-13.70,-108,-6.22"]
        lines = [l for l in csv.reader(test_line, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)]

        expected_columns = ["01005950100", "01", "005", "950100", "187.3614167", "11.21928403", "", "21640", "Eufaula, AL - GA", "", "2", "C", "3848", "1735", "3321", "1627", "-527", "-13.70", "-108", "-6.22"]
        parsed_columns = TractPopulationChangeReader().check_collumns(lines[0])
        self.assertEqual(expected_columns, parsed_columns)

    def test_invalid_parse_line(self):
        with self.assertRaises(Exception):
            invalid_file_path = "../input/InvalidColumnsData.csv"
            reader = TractPopulationChangeReader(invalid_file_path)
            processor = TractPopulationChangeProccessor()
            reader.open_and_validate_file()
            reader.readLine(processor.parse_text_to_datum)

if __name__ == '__main__':
    unittest.main()