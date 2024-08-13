import pandas as pd

path = "data/"
df = pd.read_csv(path + "Temporal Geração de Energia.csv", sep=';')

df.drop(columns=["Cor Período 2 GE", "Data Escala de Tempo 2 GE"], inplace=True)
df.rename(columns={"Data Dica Temp 2": "data", "Selecione Tipo de GE": "geracao"}, inplace=True)

df.to_csv(path + "geracao_solar.csv", sep=';')

print(df.info())
print(df.tail(5))