import conversion_modules

if __name__ == "__main__":
    print("select the Type of conversion")

    print(" 1. JSON to Excel\n 2. JSON to CSV\n 3. Multiple CSV files to Excel")
    selected_option = int(input("your option (from 1 to 3) :"))

    if selected_option == 1:
        path = str(input("Path of JSON file :"))
        sheetname  = str(input("Name of sheet (optional) :"))
        output_file = str(input("Path of Output Excel :"))
        if(sheetname == ""):
            sheetname = "sheet1"
        conversion_modules.json_toXlsx(path,output_file,sheetname)
    
    elif selected_option == 2:
        path = str(input("Path of JSON file :"))
        output_file = str(input("Path of Output CSV :"))
        conversion_modules.json_toCsv(path,output_file)

    elif selected_option == 3:
        no_of_csv_files = int(input("Number of csv files to be added :"))
        list_of_csv_files = []
        for iterator in range(no_of_csv_files):
            filename = str(input("CSV File "+str(iterator+1)+" Path :"))
            list_of_csv_files.append(filename)
        outputExcelfilename = str(input("Output Excel file name :"))
        conversion_modules.Multi_csv_toXlsx(list_of_csv_files,outputExcelfilename)
    else:
        print("invalid option :/ \n run me again! ")
        exit(0)