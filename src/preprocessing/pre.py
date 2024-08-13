import pandas as pd

path = "data/"

df = pd.read_csv(path + "Temporal Geração de Energia.csv", sep=';')



# df[['month', 'year']] = df['month_year'].str.split(' de ', expand=True)

# string_to_number = {'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}
# df['month'] = df['month'].replace(string_to_number)


print(df.tail())