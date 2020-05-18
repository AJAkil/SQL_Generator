import json

f = open('who_response.json')
data = json.load(f)

sql_str = ''

for index, value in enumerate(data):
    sql_str += 'INSERT INTO medical_data VALUES((SELECT id from regions where alpha3=\'' + value["Name"] + '\' LIMIT 1),\'' + value["Name"] + '\',' + str(value["value"])+',\'2020-04-30\');\n'



print(sql_str)