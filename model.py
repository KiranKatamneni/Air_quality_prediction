import numpy as np
import pandas as pd
import pickle

aqi = pd.read_csv('C:/Users/KIRAN/OneDrive/Desktop/datasets/city_day/city_day.csv')
aqi.head()

aqi['PM2.5'].fillna('67',inplace = True)
aqi['PM10'].fillna('118',inplace = True)
aqi['NO'].fillna('17',inplace = True)
aqi['NO2'].fillna('28',inplace = True)
aqi['NH3'].fillna('23',inplace = True)
aqi['CO'].fillna('2',inplace = True)
aqi['SO2'].fillna('14',inplace = True)
aqi['O3'].fillna('34',inplace = True)
aqi['AQI'].fillna('166',inplace = True)

aqi.isna().sum()

aqi.drop(['NOx','Benzene','Toluene','Xylene'],axis = 1,inplace = True)
aqi.head()

aqi.drop(['City','Date','AQI_Bucket'],axis = 1,inplace = True)

new = aqi.astype('int')

new.head()

X = new.drop('AQI',axis = 1)
y = new['AQI']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor()
reg.fit(X_train,y_train)

pickle.dump(reg,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

print(model.predict([[66,118,16,15,23,1,30,50]]))
