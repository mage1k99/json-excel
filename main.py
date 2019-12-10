import get_json
import json
from pandas.io.json import json_normalize

#get_json.getJson('pts','members')
# data=[]
with open('members.json') as file:
#     for line in file:
#         data.append(json.loads(line))
#pandas.read_json('exported_json.json',lines=True).to_excel('output.xlsx')
#pandas.read_json(file).to_excel("output.xlsx")
    data = json.load(file)
normalizedJson = json_normalize(data)
normalizedJson.to_csv("our.csv",index=False,sep='\t',encoding='utf-8')
normalizedJson.to_excel("ourEx.xlsx",verbose=True,sheet_name="members",encoding='utf-8')