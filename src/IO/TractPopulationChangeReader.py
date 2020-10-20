import os
import csv
import pdb
import constants as CONSTANTS
from typing import Callable, List
from Entities.PopulationChangeDatum import PopulationChangeDatum


class TractPopulationChangeReader():
    """A custom CSV file reader that is designed to read the input dataset"""

    def __init__(
            self, 
            input_file_path=os.path.join(CONSTANTS.INPUT_FILE_PATH, CONSTANTS.INPUT_FILE_NAME)
        ) -> None:
        self.input_file_path = input_file_path
        """Path of the input file"""

        self.load_input_path(input_file_path)

        
    def load_input_path(self, input_file_path: str):
        if not input_file_path:
            raise ValueError("Input File Path must not be empty!")

        if not os.path.exists(input_file_path):
            raise FileNotFoundError("Input file must exist in the specified path!")
            
        self.input_file_path = input_file_path

    def open_and_validate_file(self) -> None:
        """Validates the file format and opens the file"""
        file = open(self.input_file_path, "r")
        self.reader = csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)

        first_line = next(self.reader)
        if not first_line or ','.join(first_line) != CONSTANTS.INPUT_FILE_HEADER_ROW:
            raise Exception("Input file is invalid")

    def readLine(self, lineProcessorMethod: Callable[[List[str]], PopulationChangeDatum]) -> PopulationChangeDatum:
        """Reads a single line, parses and returns it."""
        try:
            line = next(self.reader)
            collumns = self.check_collumns(line)
            return lineProcessorMethod(collumns)
        except StopIteration:
            return None

    def check_collumns(self, collumns: List[str], override_column_count_check = False):
        """Validate collumns"""
        
        if not override_column_count_check and len(collumns) != CONSTANTS.INPUT_FILE_COLUMN_COUNT:
            raise Exception(f"Line {self.current_line} is invalid in the input file! It has {len(collumns)} instead of {CONSTANTS.INPUT_FILE_COLUMN_COUNT}")
        return collumns