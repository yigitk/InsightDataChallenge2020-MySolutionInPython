"""Name of the input file"""
INPUT_FILE_NAME = "censustract-00-10.csv"

"""Path of the input folder"""
INPUT_FILE_PATH = "../input"

"""Name of the output file"""
OUTPUT_FILE_NAME = "report.csv"

"""Path of the output folder"""
OUTPUT_FILE_PATH = "../output"

"""Header row of the CSV that is expected in the input file"""
INPUT_FILE_HEADER_ROW = "GEOID,ST10,COU10,TRACT10,AREAL10,AREAW10,CSA09,CBSA09,CBSA_T,MDIV09,CSI,COFLG,POP00,HU00,POP10,HU10,NPCHG,PPCHG,NHCHG,PHCHG"

"""Delimiter that is used in the CSV input file"""
INPUT_FILE_DELIMITER = ','

"""Column count of the input file that is expected"""
INPUT_FILE_COLUMN_COUNT = len(INPUT_FILE_HEADER_ROW.split(INPUT_FILE_DELIMITER))

"""Default culture to be used by the application"""
DEFAULT_CULTURE = "en-US"

"""Value to be ignored while checing for cell value"""
IGNORED_COLUMN_VALUE = "(X)"
