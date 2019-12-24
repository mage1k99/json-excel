import json
from pandas.io.json import json_normalize
import pandas

if __name__ == "__main__":
    inputjson = str(input("The JSON file path :"))
    outputCsv = str(input("Output CSV file :"))
    json_toCsv(inputjson,outputCsv)

def json_toCsv(input_Json_path,output_csv_path):
    #normalize the json
    if ".csv" not in output_csv_path:
        output_csv_path = output_csv_path + ".csv"
    try:
        with open(input_Json_path) as file:
            data = json.load(file)
        normalizedJson = json_normalize(data)
        normalizedJson.to_csv(output_csv_path,index=False,sep='\t',encoding='utf-8')
    except FileExistsError as identifier:
        print(identifier.errno+" Invaild path of Json")