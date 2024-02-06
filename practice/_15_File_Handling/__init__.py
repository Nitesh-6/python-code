"""
import PyPDF2
import xlrd

# to open the file and read
try:
    file_open = open("context.txt", 'rb')
    data = file_open.read()
    file_open.close()
    print(data)
except FileNotFoundError as fnf:
    print("File not found at specified path:", fnf)
except Exception as e:
    print("Exception as:", e)
else:
    print("no exception occurred")
finally:
    print("this piece of code is executed")
# open file and write. but it deletes the existing data
file_open = open("context10.txt", "w")
data = file_open.write("welcome to the python")
file_open.close()

# open file and data in the file it. it won't delete the existing data
s = "sai"
file_open = open("context10.txt", "a")
data1 = file_open.write("\n sai")
file_open.close()

# performs two operations
file_open = open("write_data0.txt", "w+")
file_open.write("write the code here")
file_open.seek(0)  # it moves the pointer to the starting point of the file
res = file_open.read()
file_open.close()
print(res)


# ------------ using function -----------------

def read_write(file, f_mode):
    file1 = open(file, f_mode)
    res1 = file1.read()
    file1.write("started coding \n")
    file1.close()
    return res1


file_loc = "write_data20.txt"
mode = "r+"
print(read_write(file_loc, mode))


with open("test.txt", "r+") as f1:
    content = f1.read()
    f1.write("\n hi bro \n")
    print(content)

# reading the pdf file single page
pdf_file = open("sample.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(pdf_file)
pdf_obj = pdf_reader.pages[0]
res = pdf_obj.extract_text()
print(res)
pdf_file.close()

# reading the all pages in pdf by using context manager
with open("sample.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)
    pdf_obj = ""
    for page in range(len(pdf_reader.pages)):
        pdf_obj = pdf_reader.pages[page].extract_text()
        print(pdf_obj)
"""
