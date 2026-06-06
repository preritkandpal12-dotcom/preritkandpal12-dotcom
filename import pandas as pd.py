import pandas as pd 
df = pd.read_csv('weather_by_cities.csv')
print(df.head())
max_temp = df['tempreature'].max()
print("The maximun tempreature recorded was:",max_temp) 
ny_weather = df[df['city'] == 'new york']
print("Here is the weather data just for new york:", ny_weather) 
print(ny_weather)