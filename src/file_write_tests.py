import unittest
import os
import csv
from IO.PopulationChangeSummaryWriter import PopulationChangeSummaryWriter
from IO.TractPopulationChangeReader import TractPopulationChangeReader
from Entities.AreaPopulationChangeSummary import AreaPopulationChangeSummary
from Processing.TractPopulationChangeSummarizer import TractPopulationChangeSummarizer
import constants as CONSTANTS

test_output_file_path = "../output/TestReport.csv"


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(test_output_file_path):
            os.remove(test_output_file_path)

    """ File should be created even for no summary is available"""

    def test_empty_result_set_test(self):
        writer = PopulationChangeSummaryWriter(test_output_file_path)
        empty_summary_dictionary = {}
        writer.WriteToFile(empty_summary_dictionary)
        self.assertTrue(os.path.exists(test_output_file_path), "No file was created for simple result set!")

    """ Basic test to see if the report.csv is created with the summary"""

    def test_simple_result_set_test(self):
        writer = PopulationChangeSummaryWriter(test_output_file_path)
        summary_dictionary = {}

        summary = AreaPopulationChangeSummary("Test", '"A test area, Test State"')
        summary.number_of_census_tracts = 2
        summary.population_percent_changes = [10.2, 15.1]
        summary.total_population_in_2000 = 11200
        summary.total_population_in_2010 = 13400
        summary.update_averages()

        summary_dictionary[summary.area_code] = summary
        writer.WriteToFile(summary_dictionary)

        self.assertTrue(os.path.exists(test_output_file_path), "No file was created for simple result set!")

    """ Test that creates an input here just to test the validity of columns"""

    def test_simple_result_set_write_and_read_test(self):
        writer = PopulationChangeSummaryWriter(test_output_file_path)
        summary_dictionary = {}

        summary = AreaPopulationChangeSummary("Test", 'A test area, Test State')
        summary.number_of_census_tracts = 2
        summary.population_percent_changes = [10.2, 15.1]
        summary.total_population_in_2000 = 11200
        summary.total_population_in_2010 = 13400
        summary.update_averages()

        summary_dictionary[summary.area_code] = summary
        writer.WriteToFile(summary_dictionary)

        self.assertTrue(os.path.exists(test_output_file_path), "No file was created for simple result set!")

        with open(test_output_file_path, 'r') as file:
            lines = [l for l in
                     csv.reader(file, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)]
            output_columns = TractPopulationChangeReader(test_output_file_path).check_collumns(lines[0], True)
            self.assertIsNotNone(output_columns, "Written file cannot be read")
            self.assertEqual(6, len(output_columns), "Written file has invalid column count")

    """Test that tests the example areas in dataset in insight/readme.md """

    def test_main_dataset_validated_test(self):
        area_code_filter = ["28540", "46900"]
        TractPopulationChangeSummarizer(area_code_filter).summarize_data_set()
        output_file_path = os.path.join(CONSTANTS.OUTPUT_FILE_PATH, CONSTANTS.OUTPUT_FILE_NAME)
        expected_result_file_path = "../input/ExpectedResult.csv"

        self.assertTrue(os.path.exists(output_file_path), "No file was created for main result set!")

        with open(output_file_path, 'r') as output_file:
            output_file_content = [l for l in
                                   csv.reader(output_file, quotechar='"', delimiter=',', quoting=csv.QUOTE_MINIMAL,
                                              skipinitialspace=True)]

            with open(expected_result_file_path, 'r') as expected_result_file:
                expected_result_file_content = [l for l in
                                                csv.reader(expected_result_file, quotechar='"', delimiter=',',
                                                           quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)]
                self.assertEqual(len(expected_result_file_content), len(output_file_content),
                                 "Generated report and expected result do not have the same row count!")
                for i in range(len(output_file_content)):
                    self.assertEqual(expected_result_file_content[i], output_file_content[i],
                                     f"Line {i + 1} do not match between expected result and generated report!")


if __name__ == '__main__':
    unittest.main()
