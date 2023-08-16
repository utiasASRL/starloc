from pathlib import Path
import os

import pandas as pd

DATASET_ROOT = str(Path(__file__).parent)


DATA_TYPES = ["uwb", "apriltag", "apriltag_cal", "imu"]
# choose any combination of DATA_TYPES
# - uwb
# - apriltag
# - apriltag_calib
# - imu
DATASET = "loop-3d_s3"
DATA = ["uwb", "apriltag"]


def read_calib(dataset_root=DATASET_ROOT, dataset=DATASET):
    import json

    fname = os.path.join(dataset_root, "data", dataset, "calib.json")
    with open(fname, "r") as f:
        calib_dict = json.load(f)
    return calib_dict


def read_params(dataset_root=DATASET_ROOT, dataset=DATASET):
    import json

    fname = os.path.join(dataset_root, "dataset_params.json")
    with open(fname, "r") as f:
        dataset_dict = json.load(f)
    return [dict_ for dict_ in dataset_dict if dict_["name"] == dataset][0]


def read_landmarks(dataset_root=DATASET_ROOT, dataset=DATASET, data=DATA):
    params = read_params(dataset_root, dataset)
    version = params["landmarks"]

    df_data = []
    for data_type in data:
        if "apriltag" in data_type:
            fname = os.path.join(
                dataset_root, "mocap", f"environment_{version}" + ".csv"
            )
            df = pd.read_csv(fname)
            df["data_type"] = data_type
            df_data.append(df)
        elif "uwb" in data_type:
            fname = os.path.join(
                dataset_root, "mocap", f"uwb_markers_{version}" + ".csv"
            )
            df = pd.read_csv(fname)
            df["data_type"] = "uwb"
            df_data.append(df)
        else:
            raise ValueError(
                f"Requested unknown data_type: {data_type}. Choose from {DATA_TYPES}."
            )
    return pd.concat(df_data)


def read_data(dataset_root=DATASET_ROOT, dataset=DATASET, data=DATA):
    df_data = []
    for data_type in data:
        fname = os.path.join(dataset_root, "data", dataset, data_type + ".csv")
        df = pd.read_csv(fname)
        df["data_type"] = data_type
        df_data.append(df)
    return pd.concat(df_data)


if __name__ == "__main__":
    landmarks = read_landmarks()
    data = read_data()
    print("read landmarks:\n", landmarks)
    print("read data:\n", data)
    print("done")
