#import csv and pandas as pd
import csv
import pandas as pd

data = pd.read_csv('crop.csv')
data.columns
data.rename(columns={'APPLES - PRODUCTION, MEASURED IN $  -  <b>VALUE</b>':'Apple Production $'}, inplace=True)
cleaned_data = pd.DataFrame({'production':data['Apple Production $']})
cleaned_data.describe()
cleaned_data = pd.DataFrame({'production':data['Apple Production $'], 'year': data['Year']})

from bokeh.charts import Line, output_file, save, Bar
l = Line(cleaned_data, x='year', y='production')
output_file('line.html')
save(l)


