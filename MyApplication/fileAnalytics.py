import pandas as pd
import numpy as np

def fileAnalytics(file_path):
    data = pd.read_csv(file_path, sep=" ")
    return data.shape