# .............................................
# This file contains the paths to various directories and files used in the project. It defines the project root directory, data folders, input files, and output files.
# ..............................................


from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ----------------------------
# Data folders
# ----------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
CLEANED_DATA_DIR = DATA_DIR / "cleaned"
FEATURE_DATA_DIR = DATA_DIR / "features"
STATS_DATA_DIR = DATA_DIR / "stats"

# ----------------------------
# Input files
# ----------------------------

RAW_DATA = RAW_DATA_DIR / "fashion_posts_raw.json"

# ----------------------------
# Output files
# ----------------------------
