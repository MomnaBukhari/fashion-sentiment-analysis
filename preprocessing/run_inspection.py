# .............................................
# This file is used to run data inspection on the dataset.
# It loads the raw data, creates a DataInspector instance, and runs all inspection methods.
# ..............................................


import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from load_data import DataLoader
from inspect_data import DataInspector
from config.paths import RAW_DATA

def main():
    print(RAW_DATA)
    loader = DataLoader(RAW_DATA)
    df = loader.load_json()
    inspector = DataInspector(df)
    inspector.run_all()

if __name__ == "__main__":
    main()