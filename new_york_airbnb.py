import numpy as mynp
import pandas as mypd
import matplotlib.pyplot as mympl
import seaborn as mysbn
import math

df = mypd.read_csv('Newyorkairbnbdata.csv')
df_visual = df

df.drop(['host_id','latitude','longitude'], inplace=True, axis=1)

df.isnull().sum()

price_avg = df["price"].mean()
df["price"].fillna(price_avg, inplace = True)

avail_avg = df["availability_365"].mean()
df["availability_365"].fillna(avail_avg, inplace = True)

df[df.duplicated()]

df.drop_duplicates(inplace = True)

df.boxplot()

mysbn.boxplot(y=df["price"])


from pandas.core.groupby import grouper
group = ['Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Bronx']
df_visual["neighbourhood_group"].plot(kind = 'hist') #is in numeric value
mympl.title("Number of available Airbnb in each Neighbourhood")
mympl.xlabel('Neighbourhood Group') 
mympl.ylabel('Number of Airbnb')
mympl.grid()

a = df_visual['room_type'].value_counts()
room = ['Private room','Entire home/apt','Shared room']
cols = ['c', 'r', 'm']
mympl.figure(figsize=(5,5))
mympl.pie(a,labels=room,colors=cols,explode=(0.0,0.0,0.0),autopct='%1.2f%%')
mympl.title('Room Type in Airbnb')
mympl.show()

x = df_visual['neighbourhood']
y = df_visual['price']

mympl.scatter(x, y, label='Ney York neighbourhood', color='c')
mympl.xlabel('Neighbourhood')
mympl.ylabel('Price(USD)')
mympl.title('Scatter Plot')
mympl.legend()
mympl.show()

mysbn.barplot(data = df_visual,x = 'neighbourhood_group', y = 'number_of_reviews')

mysbn.violinplot(x = df_visual['number_of_reviews'], palette = 'rainbow');
