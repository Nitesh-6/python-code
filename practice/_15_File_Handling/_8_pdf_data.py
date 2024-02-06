import zipfile

'''
import PyPDF2
# python -m pip install PyPDF2  (site-packages)
# how to read data from pdf file in python
pdfFileObj = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("Pages:", pdfReader.numPages)

for p_no in range(0, pdfReader.numPages):
    print("****** Content of Page ******:", p_no)
    p_data = pdfReader.getPage(p_no)
    # algorithm
    print("----------PageNo : ----------", p_no)
    data = p_data.extractText()
    print("DATA : ", data)
    # algorithm
pdfFileObj.close()
'''

'''
1. Extract zip file. Will get list of files
2. Load each file
3. Read content from each file and store into dictionary`


import zipfile
my_zip = zipfile.ZipFile('my_zip_file.zip')  # Specify your zip file's name here
storage_path = '.'
for file in my_zip.namelist():
    if my_zip.getinfo(file).filename.endswith('.txt'):
        my_zip.extract(file, storage_path) # extract the file to current folder if it is a text file
'''

'''
1. Zip File 
    - 10 folders 
        - each folder 
            - 2 txt files
            - 2 pdf files
            - 2 excel files 
    
Output: 
--------------------
data.zip    Python   introduction.txt   Content
data.zip    Python   variables.txt      Content
data.zip    Python   object.pdf         Content
data.zip    Python   about.pdf          Content
data.zip    Python   edata.xls          Content
data.zip    Python   mydata.xls         Content


Tasks division:
------------------
T1. Extract folders from zip file 
T2. Extract files from folder 
T3: Load each file and read content 
T4: Validate data 
T5: Retrieve data 
T6: Save data to db 
T7: Display final results to UI
 
'''


# zip_file =  remote server
with zipfile.ZipFile('_02_ Variables_Notes.zip', 'r') as zip_ref:
    zip_ref.extractall()
