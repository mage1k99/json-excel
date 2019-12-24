from pandas import ExcelWriter
import pandas

def Multi_csv_toXlsx(arrayOf_CSV_Filepaths,outputExcelName):
    if ".xlsx" not in outputExcelName:
        outputExcelName = outputExcelName + ".xlsx"
        try:
            with ExcelWriter(outputExcelName) as xlWriter:
                for CSVfile in arrayOf_CSV_Filepaths:
                    pandas.read_csv(CSVfile).to_excel(xlWriter,sheet_name=CSVfile)
        except FileExistsError as identifier:
            print("incorrect file name")
    print("successfully converted to Excel at "+outputExcelName)

if __name__ == "__main__":
    no_of_csv_files = int(input("Number of csv files to be added :"))
    list_of_csv_files = []
    for iterator in range(no_of_csv_files):
        filename = str(input("CSV File "+(iterator+1)+" Path :"))
        list_of_csv_files.append(filename)
    outputExcelfilename = str(input("Output Excel file name :"))
    Multi_csv_toXlsx(list_of_csv_files,outputExcelfilename)