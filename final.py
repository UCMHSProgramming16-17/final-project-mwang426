#import csv and pandas as pd
import csv
import pandas as pd

#import and read data
data = pd.read_csv('crop.csv')
data.columns
#rename production column to make it simplier)
data.rename(columns={'APPLES - PRODUCTION, MEASURED IN $  -  <b>VALUE</b>':'Apple Production $'}, inplace=True)
cleaned_data = pd.DataFrame({'production':data['Apple Production $']})
cleaned_data.describe()
cleaned_data = pd.DataFrame({'production':data['Apple Production $'], 'year': data['Year']})
#import line and bar
from bokeh.charts import Line, output_file, save, Bar
l = Line(cleaned_data, x='year', y='production', title = 'Apples line graph', Color='blue')
output_file('line.html')
save(l)

b = Bar(cleaned_data, xlabel='year', ylabel='production', title = 'Apple Production Bar Graph')
output_file('bar.html')
save(b)