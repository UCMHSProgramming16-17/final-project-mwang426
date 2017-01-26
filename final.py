#import csv
import csv
#import pandas as pd
import pandas as pd

#open the data file and read it
f = open('crop.csv')
csv_f = csv.reader(f)
production = []
year = []

#print production numbers 
for row in csv_f:
    print(row[1])
    production.append(row[18])
print(production)

#makes the DataFrame
df = pd.DataFrame({
    'APPLES - PRODUCTION, MEASURED IN $  -  <b>VALUE</b>': production
})

#import line chart commands
from bokeh.charts import Line, output_file, save

#create and format the chart that is going to be apples_line.html
Linechart = Line(df, 'APPLES - PRODUCTION, MEASURED IN $  -  <b>VALUE</b>', title = 'Apple Production Line Chart', xlabel = 'year', ylabel = 'Apple production measured in $')

#make the file apples_line.html 
output_file('apples_line.html')
save(Linechart)

#import second chart commands, bar graph
from bokeh.charts import Bar, output_file, save

#create and format the bar graphs so that it is going to be apples_line.html
Bargraph = Bar(df, 'APPLES - PRODUCTION, MEASURED IN $  -  <b>VALUE</b>', title = 'Apple Proudction Bar Graph', xlabel = 'year', ylabel = 'Apples produced measured in $')

#make the file apples_bar.html
output_file('apples_bar.html')
save(Bargraph)

#import third chart commands, step graph