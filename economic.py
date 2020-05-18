import pandas as pd

f1 = open('literacy3.sql', 'w+')
f2 = open('internet.sql', 'w+')

df = pd.read_csv('nai_2.csv')
sql1 = ''
sql2 = ''

for index, value in df.iterrows():
    #sql1 += 'UPDATE economic set literacy_rate={} where region_id={};\n'.format(value['lr'], value['id'])
    sql1 += 'Insert into economic values({},\'{}\',{},null,null,1,\'{}\',\'{}\',null);\n'.format(value['id'],value['Latest_year'],value['LR'],value['iso2'],value['code'])

f1.write(sql1)
f2.write(sql2)
