import pandas as pd


url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)


#print(df.head())

#print(df.index)

print(df.columns)

#print(df.dtypes)

#print(df.info)

#print(df.isna().sum())


#print(df.isna().sum()/len(df)*100)

#print(df.describe())

#print(df.describe(include='all'))

#print (df.loc[0])

#print(df.loc[0:6:1])
#print(df.loc[:,"val_pm10"])

#ne fonctionne pas
'''
print(df.loc[1:4,["lib_zone","pm_10"]])
'''

#print(df.iloc[0])
#print(df.iloc[:,1])

#print(df.isin([0]))
#print(df.agg('val_pm10'))

#print(df.groupby(['val_pm10']).mean()[['lib_zone']])


data=df.groupby(['lib_zone']).mean()[['val_pm10']]
data['villes']=data.index
print(data)
print(data.plot.bar(x='villes',y='val_pm10',rot=0))



