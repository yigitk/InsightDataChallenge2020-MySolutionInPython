from typing import List

class AreaPopulationChangeSummary():    
    def __init__(self, area_code: str, area_description: str) -> None:
        self.area_code = area_code
        """Core Based Statstical Area Code (i.e., CBSA09)"""

        self.area_description = area_description
        """Core Based Statistical Area Code Title (i.e., CBSA_T)"""

        self.number_of_census_tracts: int = 0
        """Total number of census tracts"""

        self.total_population_in_2000: int = 0
        """Total population in the CBSA in 2000"""

        self.total_population_in_2010: int = 0
        """Total population in the CBSA in 2010"""

        self.average_population_percent_change: float = 0.0
        """Average population percent change for census tracts in this CBSA."""

        self.population_percent_changes: List[float] = []
        """List of all population change percentages belonging to the area"""
    
    def update_averages(self):
        self.average_population_percent_change = sum(self.population_percent_changes) / self.number_of_census_tracts