from math import ceil
import os
import pdb
import constants as CONSTANTS
from Entities.AreaPopulationChangeSummary import AreaPopulationChangeSummary
from pathlib import Path
from typing import Dict
from decimal import Decimal, ROUND_HALF_UP

"""A custom CSV file writer that is designed to write the output report"""


class PopulationChangeSummaryWriter():

    def __init__(
            self,
            output_file_path=os.path.join(CONSTANTS.OUTPUT_FILE_PATH, CONSTANTS.OUTPUT_FILE_NAME)
    ) -> None:
        if (not output_file_path):
            raise ValueError("Output File Path must not be empty!")
        """Path of the output file"""
        self.output_file_path = output_file_path

        """Directory of the output file"""
        self.output_dir = os.path.dirname(output_file_path)

    def make_path_if_not_exists(self):
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

    def WriteToFile(self, areaBasedSummaries: Dict[str, AreaPopulationChangeSummary]):
        self.make_path_if_not_exists()

        with open(self.output_file_path, "w") as output_file:
            keys = sorted(areaBasedSummaries.keys())
            for area_code in keys:
                summary = areaBasedSummaries[area_code]
                summary.update_averages()
                decimal_value = Decimal(summary.average_population_percent_change)
                columns = [
                    summary.area_code,
                    f'"{summary.area_description}"',
                    str(summary.number_of_census_tracts),
                    str(summary.total_population_in_2000),
                    str(summary.total_population_in_2010),
                    format(round(decimal_value, 2)).rstrip('0').rstrip('0').rstrip('.')
                ]
                output_file.write(','.join(columns) + '\n')
