import pandas as pd
import numpy as np
import os

csv_files = [file for file in os.listdir("backend/Data_git/") if file.endswith(".csv")]

df_list = [pd.read_csv(os.path.join("backend/Data_git/", file)) for file in csv_files]
merged_df = pd.concat(df_list, ignore_index=True)

merged_df.to_csv("merged_game_data.csv", index=False)
