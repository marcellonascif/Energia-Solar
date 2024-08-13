import pandas as pd

path = "data/"
df = pd.read_csv(path + "geracao_solar.csv", sep=';')

df.rename(columns={"Unnamed: 0": "id"}, inplace=True)

df["data"] = pd.to_datetime(df["data"], format="%Y-%m-%d")
# df.set_index("data", inplace=True)

print(df.info())
