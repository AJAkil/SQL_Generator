import pandas as pd

f = open('humidity.sql', 'w+')

df = pd.read_csv('country_avghum.csv')
sql = ''

for index, value in df.iterrows():
    sql += 'UPDATE environmental set avg_humidity={} where region_id={};\n'.format(value['Avg. Humidity'], value['id'])

f.write(sql)