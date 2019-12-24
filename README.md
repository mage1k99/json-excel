# :sparkles: json-excel :sparkles:
Simple python scripts to convert :
* JSON to Excel :white_check_mark:
* JSON to CSV :white_check_mark:
* Multiple CSV to single Excel :white_check_mark:
:relieved: 
----

## How to Use :question: ##

### Convert on the Go ###

1. Clone the modules and navigate

2. Run `python3 main.py `
    1. select the requied option 
    2. enter the **file name as absolute path if it exist on other directories**
    (for windows users)
    for eg: 
    if the file is loacated at C:\Documents\collection.json
    And You want the generated output file at C:\Documents\exported\output.xlsx
      ```
          C:\Users\Mage1k99\json-excel>python3 main.py
          1. JSON to Excel
          2. JSON to CSV
          3. Multiple CSV files to Excel
          your option (from 1 to 3) : 1
          Path of JSON file : C:\Users\Documents\collection.json
          Sheetname (optional) : mysheet
          Path of Output Excel :C:\Users\Documents\output.xlsx 
      ```
      (for linux and mac users)
      eg:
      if the input file is located at ~/json/inputcollection.json
      And the output file (xlsx) to be generated at ~/excel/outputexcel.xlsx
      ```
          mage:~/json-excel$ python3 main.py
          1. JSON to Excel
          2. JSON to CSV
          3. Multiple CSV files to Excel
          your option (from 1 to 3) : 1
          Path of JSON file : ~/json/outputexcel.xlsx
          Sheetname (optional) : mysheet
          Path of Output Excel : ~/excel/outputexcel.xlsx 
      ```
> :exclamation: check to be done before conversion :exclamation:
  > * use python3, (as python2.7 will reach its [end of life](https://pythonclock.org)
  > * Always add ___extension to the filepaths while using___ 
  > * before entering output path make sure that the directory exist!
  > * Give the correct file and path name

### using as seprate modules ###

Just use the conversion module in your own projects by importing

----

### screenshots ###
screenshot of running main.py with files in absolute path

![screenshot of running main.py](https://github.com/mage1k99/image_hostingRepo/blob/master/json-excel_asserts/Screenshot.png "Screenshot of running main.py")

![screenshot of genrated output from main.py](https://github.com/mage1k99/image_hostingRepo/blob/master/json-excel_asserts/generated_output.png "screenshot of output")

----
### Requirements ###

* pandas
* openpyxl
* setuptools

`pip3 install -r requirements.txt`

 Based on python library pandas
 
 ----
 ##### Contributions are welcomed :smile:  ####
 
 Feel free to 
 * Fork, modify to add feature and make pull request :clap:
 * report bugs, request feature through issues :clap:
 
 ##### Thank you for using and spending your time with this project :sparkling_heart: #####