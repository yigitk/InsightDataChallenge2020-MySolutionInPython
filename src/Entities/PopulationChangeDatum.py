class PopulationChangeDatum():
    """Representation of a single data record in the Population Change Dataset"""
    
    def __init__(self) -> None:
        self.geo_id: str
        """GEOID	Concatenated State-County-Census Tract Code"""   

        self.state_fips_code: str
        """ST10	State FIPS Code"""   

        self.county_fips_code: str
        """COU10	County FIPS Code"""   

        self.tract_code: str
        """TRACT10	Census Tract Code"""   

        self.land_area: float
        """AREAL10	Land area (square miles)"""    

        self.water_area: float
        """AREAW10	Water area (square miles)"""    

        self.combined_area_code: str
        """CSA09	Combined Statistical Area Code"""    

        self.core_based_area_code: str
        """CBSA09	Core Based Statistical Area (CBSA) Code"""    

        self.core_based_area_title: str
        """CBSA_T	Core Based Statistical Area Title"""    

        self.metropolitan_division_code: str
        """MDIV09	Metropolitan Division Code"""    

        self.cbsa_status_indicator: int
        """CSI	CBSA Status Indicator (1=Metropolitan statistical area, 2=Micropolitan statistical area, 3=Outside CBSA)"""    

        self.central_or_outlying_country_flag: str
        """COFLG	Central/Outlying County Flag (C=Central county, O=Outlying county)"""    

        self.total_population_in_2000: int
        """POP00	Total population (2000)"""    

        self.total_housing_units_in_2000: int
        """HU00	Total housing units (2000)"""    

        self.total_population_in_2010: int
        """POP10	Total population (2010)"""    

        self.total_housing_units_in_2010: int
        """HU10	Total housing units (2010)"""    

        self.numeric_population_change: int
        """NPCHG	Numeric population change: 2000 to 2010"""    

        self.percentage_population_change: float
        """PPCHG	Percent population change: 2000 to 2010"""    

        self.numeric_housing_units_change: int
        """NHCHG	Numeric change in housing units: 2000 to 2010"""    

        self.percentage_housing_units_change: float
        """PHCHG	Percent change in housing units: 2000 to 2010"""    
