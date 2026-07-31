# .............................................
# This file is used to load the raw JSON dataset into a Pandas DataFrame.
# It includes a DataLoader class that takes the file path as input and provides a method to
# load the JSON data into a DataFrame. The class also checks if the file exists and raises an error if it does not.
# .............................................


from pathlib import Path
import json
import pandas as pd


class DataLoader:
    
    def __init__(self, file_path):
        self.file_path = Path(file_path)
    def load_json(self):
        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)
        df = pd.DataFrame(data)
        print("Dataset successfully loaded.")

        return df


    # Used while feature engineering to load the cleaned dataset from CSV file.
    def load_csv(self):

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        df = pd.read_csv(
            self.file_path,
            encoding="utf-8"
        )

        print("CSV dataset successfully loaded.")

        return df