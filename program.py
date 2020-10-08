
import pandas as pd
import sys;
import numpy as np;
import argparse;
import matplotlib.pyplot as plt;

url = "https://opendata.arcgis.com/datasets/6f64bbd4f94c425791c2ec7eee33bb71_0.csv"
df = pd.read_csv(url)

df.head()



'''niveau de val pour qualite
---------------------------

data = df.groupby(['valeur']).mean()[["val_no2", "val_so2"]]
data.plot.bar(stacked=True)'''

'''
#Camembert 
-------------
data = df.groupby(['lib_zone']).mean()['valeur'] 
data.plot.pie(figsize=(11, 11))
plt.legend()

plt.title(" Moyenne de la qualité del'air par ville  en Région centre 2018-2019")'''



#Moyenne des poluants determinant la qualite de l air 
#--------------

data = df.groupby(['qualif']).mean()[['val_no2', 'val_so2',"val_o3","val_pm10","val_pm25"]]
data.plot.barh(stacked=True)
plt.legend()
plt.xlabel("Valeurs")
plt.ylabel("Qualité de l'air")
plt.title("Répartion des poluants déterminants la qualité de l'air en région centre ")