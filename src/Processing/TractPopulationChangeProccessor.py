import constants as CONSTANTS
from Entities.PopulationChangeDatum import PopulationChangeDatum
from typing import List
"""Check if string is float"""
def is_float(string: str):
    
    try:
        float(string.replace(',',''))
        return True
    except:
        return False
"""Check if string is int"""
def is_int(string: str):
    
    try:
        int(string.replace(',',''))
        return True
    except:
        return False
 """Parse string to float"""
def to_float(string: str):
   
    try:
        return float(string.replace(',',''))
    except:
        return float(0)
 """Parse string to int"""
def to_int(string: str):
   
    try:
        return int(string.replace(',',''))
    except:
        return 0

class TractPopulationChangeProccessor():
    """Normalize the string value removing double quotes"""
    def normalize_numeric_value(self, raw_value: str):
        
        if raw_value and raw_value.startswith('"') and raw_value.endswith('"'):
            return raw_value[1: len(raw_value) - 2]
        return raw_value
		"""
		Parse all the columns base on the table:
		Variable    Variable Description
		GEOID	    Concatenated State-County-Census Tract Code
		ST10	    State FIPS Code
		COU10	    County FIPS Code
		TRACT10	    Census Tract Code
		AREAL10	    Land area (square miles)
		AREAW10	    Water area (square miles)
		CSA09	    Combined Statistical Area Code
		CBSA09	    Core Based Statistical Area (CBSA) Code
		CBSA_T	    Core Based Statistical Area Title
		MDIV09	    Metropolitan Division Code
		CSI	    CBSA Status Indicator (1=Metropolitan statistical area, 2=Micropolitan statistical area, 3=Outside CBSA)
		COFLG	    Central/Outlying County Flag (C=Central county, O=Outlying county)
		POP00	    Total population (2000)
		HU00	    Total housing units (2000)
		POP10	    Total population (2010)
		HU10	    Total housing units (2010)
		NPCHG	    Numeric population change: 2000 to 2010
		PPCHG	    Percent population change: 2000 to 2010

		NHCHG	    Numeric change in housing units: 2000 to 2010
		PHCHG	    Percent change in housing units: 2000 to 2010
		"""
    def parse_text_to_datum(self, line_columns: List[str]) -> PopulationChangeDatum:
       
        geo_id = line_columns[0]
        state_fips_code = line_columns[1]
        county_fips_code = line_columns[2]
        census_tract_code = line_columns[3]
        land_area_string = self.normalize_numeric_value(line_columns[4])
        
        if land_area_string and land_area_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_float(land_area_string):
            raise ArithmeticError(f"Land Area info is set to {land_area_string} which is invalid!")

        land_area = to_float(land_area_string)

        water_area_string = self.normalize_numeric_value(line_columns[5])

        if water_area_string and water_area_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_float(water_area_string):
            raise ArithmeticError(f"Water Area info is set to {water_area_string} which is invalid!")

        water_area = to_float(water_area_string)

        combined_area_code = line_columns[6]
        coreBased_area_code = line_columns[7]
        coreBased_area_title = line_columns[8]
        metropolitan_division_code = line_columns[9]
        cbsa_status_indicator_string = line_columns[10]

        if cbsa_status_indicator_string and cbsa_status_indicator_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(cbsa_status_indicator_string):
            raise ArithmeticError(f"CBSA Status Indicator is set to {cbsa_status_indicator_string} which is invalid!")

        cbsa_status_indicator = to_int(cbsa_status_indicator_string)

        central_or_outlying_county_flag = line_columns[11]

        total_population_in_2000_string = self.normalize_numeric_value(line_columns[12])
        if total_population_in_2000_string and total_population_in_2000_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(total_population_in_2000_string):
            raise ArithmeticError(f"Total Population in 2000 is set to {total_population_in_2000_string} which is invalid!")

        total_population_in_2000 = to_int(total_population_in_2000_string)

        total_housing_units_in_2000_string = self.normalize_numeric_value(line_columns[13])
        if total_housing_units_in_2000_string and total_housing_units_in_2000_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(total_housing_units_in_2000_string):
            raise ArithmeticError(f"Total Housing Units in 2000 is set to {total_population_in_2000_string} which is invalid!")
        
        total_housing_units_in_2000 = to_int(total_housing_units_in_2000_string)

        total_population_in_2010_string = self.normalize_numeric_value(line_columns[14])
        if total_population_in_2010_string and total_population_in_2010_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(total_population_in_2010_string):
            raise ArithmeticError(f"Total Population in 2010 is set to {total_population_in_2010_string} which is invalid!")

        total_population_in_2010 = to_int(total_population_in_2010_string)


        total_housing_units_in_2010_string = self.normalize_numeric_value(line_columns[15])
        if total_housing_units_in_2010_string and total_housing_units_in_2010_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(total_housing_units_in_2010_string):
            raise ArithmeticError(f"Total Housing Units in 2010 is set to {total_housing_units_in_2010_string} which is invalid!")
        
        total_housing_units_in_2010 = to_int(total_housing_units_in_2010_string)


        numeric_population_change_string = self.normalize_numeric_value(line_columns[16])
        if numeric_population_change_string and numeric_population_change_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(numeric_population_change_string):
            raise ArithmeticError(f"Numeric Population Change is set to {numeric_population_change_string} which is invalid!")
        numeric_population_change = to_int(numeric_population_change_string)


        percent_population_change_string = self.normalize_numeric_value(line_columns[17])
        if percent_population_change_string and percent_population_change_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_float(percent_population_change_string):
            raise ArithmeticError(f"Percent Population Change is set to {percent_population_change_string} which is invalid!")
        percent_population_change = to_float(percent_population_change_string)

        numeric_housing_units_change_string = self.normalize_numeric_value(line_columns[18])
        if numeric_housing_units_change_string and numeric_housing_units_change_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_int(numeric_housing_units_change_string):
            raise ArithmeticError(f"Numeric Housing Units Change is set to {numeric_housing_units_change_string} which is invalid!")
        numeric_housing_units_change = to_int(numeric_housing_units_change_string)

        percent_housing_units_change_string = self.normalize_numeric_value(line_columns[19])
        if percent_housing_units_change_string and percent_housing_units_change_string != CONSTANTS.IGNORED_COLUMN_VALUE and not is_float(percent_housing_units_change_string):
            raise ArithmeticError(f"Percent Housing Units Change is set to {percent_housing_units_change_string} which is invalid!")
        percent_housing_units_change = to_float(percent_housing_units_change_string)
        
        change_datum = PopulationChangeDatum()
        change_datum.geo_id = geo_id
        change_datum.state_fips_code = state_fips_code
        change_datum.county_fips_code= county_fips_code
        change_datum.tract_code = census_tract_code
        change_datum.land_area = land_area
        change_datum.water_area = water_area
        change_datum.cbsa_status_indicator = cbsa_status_indicator
        change_datum.central_or_outlying_country_flag = central_or_outlying_county_flag
        change_datum.combined_area_code = combined_area_code
        change_datum.core_based_area_code = coreBased_area_code
        change_datum.core_based_area_title = coreBased_area_title
        change_datum.metropolitan_division_code = metropolitan_division_code
        change_datum.numeric_housing_units_change = numeric_housing_units_change
        change_datum.numeric_population_change = numeric_population_change
        change_datum.percentage_housing_units_change = percent_housing_units_change
        change_datum.percentage_population_change = percent_population_change
        change_datum.total_housing_units_in_2000 = total_housing_units_in_2000
        change_datum.total_housing_units_in_2010 = total_housing_units_in_2010
        change_datum.total_population_in_2000 = total_population_in_2000
        change_datum.total_population_in_2010 = total_population_in_2010

        return change_datum
