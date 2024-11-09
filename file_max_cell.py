import pandas as pd

def file_max_cell (filename, column):
    df = pd.read_csv("scores.csv")
    max = df[column].max()
    row = df[column==max]





