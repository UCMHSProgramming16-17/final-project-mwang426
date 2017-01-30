#import csv and pandas as pd
import csv
import pandas as pd

#read csv dataframe
data = pd.read_csv('crop.csv')
data.columns

#rename production column to make it simplier)
data.rename(columns={'APPLES - PRODUCTION, MEASURED IN $  -  <b>VALUE</b>':'Apple Production $'}, inplace=True)
cleaned_data = pd.DataFrame({'production':data['Apple Production $']})
#check to see if the data is renamed
cleaned_data.describe()
cleaned_data = pd.DataFrame({'production':data['Apple Production $'], 'year': data['Year']})

nums = []
for n in list(cleaned_data['production']):
    n2 = ''
    for char in n:
        if char != ',':
            n2 += char
    print(n2)
    nums.append(int(n2))
print(nums)
cleaned_data['production'] = nums

#import line chart and bar graph from bokeh
from bokeh.charts import Line, output_file, save, Bar, save

#set up the bar graph with specific parameters. Bar graph is used to show simply how much production per year
b = Bar(cleaned_data, label = 'year', values = 'production', title = 'Apple Production Bar Graph', outline_line_color ='blue', background_fill_color = 'pink', yscale='linear')
#create the output file and save the bar graph to the output file
output_file('bar.html')
save(b)

#set up the parameters of the line chart. Line chart is used to show the trend throughout the years
l = Line(cleaned_data, x='year', y='production', title = 'Apples line graph', outline_line_color ='blue', yscale='linear')
#create the output file
output_file('line.html')
#save the line graph to the output file
save(l)

#import donut from bokeh
from bokeh.charts import Donut, output_file, save
#import palettes from bokeh to use in parameters
from bokeh.palettes import magma
#set up donut with parameters to show how apple productions remain relatively similar in number throughout the years
d = Donut(cleaned_data, label = 'year', title = 'Year by production', text_font_size='9pt', hover_text='year' and 'production', palette=magma(8))
#create the output file and save the donut chart to the output file
output_file('donut.html')
save(d)