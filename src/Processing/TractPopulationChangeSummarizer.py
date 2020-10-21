import pdb
from typing import Dict, List
from Entities.PopulationChangeDatum import PopulationChangeDatum
from Entities.AreaPopulationChangeSummary import AreaPopulationChangeSummary
from IO.TractPopulationChangeReader import TractPopulationChangeReader
from IO.PopulationChangeSummaryWriter import PopulationChangeSummaryWriter
from Processing.TractPopulationChangeProccessor import TractPopulationChangeProccessor

"""Class responsible for orchestrating the complete flow of summarization of the dataset"""


class TractPopulationChangeSummarizer():
    area_based_population_changes: Dict[str, AreaPopulationChangeSummary]
    area_code_filter: List[str]
    reader = TractPopulationChangeReader()
    processor = TractPopulationChangeProccessor()

    """Filter of area codes"""

    def __init__(self, area_codes: List[str] = []) -> None:
        self.area_code_filter = area_codes

    """
    Executes the flow of parsing the input file, summarizing the dataset for the required output
    and finally saving the result in the output file
    """

    def summarize_data_set(self):

        self.area_based_population_changes = {}
        self.reader.open_and_validate_file()
        while True:
            population_change = self.reader.readLine(self.processor.parse_text_to_datum)
            if population_change == None:
                break

            if population_change.core_based_area_code and (
                    len(self.area_code_filter) == 0 or population_change.core_based_area_code in self.area_code_filter
            ):
                self.process_datum(population_change)
        PopulationChangeSummaryWriter().WriteToFile(self.area_based_population_changes)

    """Processes a single record that was fetched from the input file and adds in to the overall summary"""

    def process_datum(self, population_change: PopulationChangeDatum):

        summary = AreaPopulationChangeSummary(population_change.core_based_area_code,
                                              population_change.core_based_area_title)

        if population_change.core_based_area_code in self.area_based_population_changes:
            summary = self.area_based_population_changes[population_change.core_based_area_code]

        summary.total_population_in_2000 += population_change.total_population_in_2000
        summary.total_population_in_2010 += population_change.total_population_in_2010
        summary.number_of_census_tracts += 1
        summary.population_percent_changes.append(population_change.percentage_population_change)
        self.area_based_population_changes[population_change.core_based_area_code] = summary
