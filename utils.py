import pandas as pd


def load_challenge_data(filename="~/Desktop/reverie/reverie_challenge_data.csv"):
    df = pd.read_csv(filename, header=[0, 1])
    return df


def get_assay_data(assay):
    data = load_challenge_data("~/Desktop/reverie/reverie_challenge_data.csv")
    measured_index = ("measured_values", assay)
    predicted_index = ("predicted_values", "model_for_" + assay)
    return data[measured_index], data[predicted_index]
