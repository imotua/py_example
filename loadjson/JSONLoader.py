import os
import pandas as pd
import json


class JSONLoader:

  # initialize class with root_dir
    def __init__(self, root_dir):
        self.root_dir = root_dir

    # read_json_files method
    def getDataframe(self, filename):
        dataframes = []
        if filename.endswith('.json'):
            file_path = os.path.join(self.root_dir, filename)
            # Open the file and read line by line
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # Load each line as a JSON object and append to the list
                    data = json.loads(line)
                    df = pd.json_normalize(data)
                    dataframes.append(df)
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df

    # read_json_files multiple files method
    def getDataframes(self):
        dataframes = []
        for subdir, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(subdir, file)
                    with open(file_path) as f:
                        data = json.load(f)
                        df = pd.json_normalize(data)
                        dataframes.append(df)
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df
