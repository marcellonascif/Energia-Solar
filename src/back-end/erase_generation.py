import numpy as np
import pandas as pd
import random

def erase(df: pd.DataFrame, column: str, iter: int=1):
    '''
    Function to erase some data from the DataFrame
    '''

    for i in range(iter):
        line = random.randint(0, len(df) - 1)
        df.loc[line, column] = np.nan

    return df


path = "data/"
df = pd.read_csv(path + "geracao_solar.csv", sep=';')

df.rename(columns={"Unnamed: 0": "id"}, inplace=True)

df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")

df = erase(df, "geracao", len(df) // 10)

print(df.info())

df.to_csv(path + "geracao_solar_faltante.csv", sep=";", index=False, encoding="utf-8")
