from pathlib import Path
import os

import pandas as pd

dataset_root = str(Path(__file__).parent)


MAPPING = {
        "loop-3d_s1": "environment_v1"
}

def read_landmarks(dataset_root, dataset="loop-3d_s1"):
    environment_type = MAPPING[dataset]
    fname = os.path.join(dataset_root, "mocap", environment_type + ".csv")
    df = pd.read_csv(fname)
    return df

def read_data(dataset_root=dataset_root, dataset="loop-3d_s1", data=["uwb", "stereo"]):
    df_data = [] 
    for data_type in data:
        fname = os.path.join(dataset_root, "data", data_type + ".csv")
        df = pd.read_csv(fname)
        df_data.append(df)
    return pd.concat(df_data)

if __name__ == "__main__":
    landmarks = read_landmarks()
    data = read_data()
