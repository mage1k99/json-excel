import json
from pandas.io.json import json_normalize
import pandas

if __name__ == "__main__":
    jsonpath = str(input("path to json file :"))
    outpath = str(input("output path of excel file :"))
    sheetname = str(input("enter the sheetname (optional)"))
    if sheetname == "":
        sheetname = "sheet1"
    json_toXlsx(jsonpath,outpath,sheetname)

def json_toXlsx(Json_path,output_excel,sheetname):
    #checking if the output has extension with it
    if ".xlsx" not in output_excel:
        output_excel = output_excel+".xlsx"
    #normalize the json
    try:
        with open(Json_path) as file:
            data = json.load(file)
        normalizedJson = json_normalize(data)
        normalizedJson.to_excel(output_excel,verbose=True,sheet_name=sheetname,encoding='utf-8')
    except FileNotFoundError as identifier:
        print("incorrect file path")