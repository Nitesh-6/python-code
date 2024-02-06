'''
gmail signup : CREATE
gmail login  : RETRIEVE
changing password : UPDATE
Deactivating account: DELETE
'''

'''
Frontend          Backend
----------------------------------------
Client      Server       Backend
------    ----------    --------------
UI  --->   PYTHON    ---> Database
           (CSD)
           
          C   S   D
          ------------
          Controller              : Controls the flow(request/response)
          Service                 : Implements business logic 
          DAO(Data Access Object) : Interacts with DB for CRUD ops 
                        Loose Coupling 
          ------------------------
            remote machine directory path
              http://devhost:80/opt/dev/naukri/madhunettem/

File : Read/Write/Execute


File attributes -
==================
filename       'myfile'
fextension     'txt'
fcontent       base64 encoded
size           '60kb'
uploaded by    'madhunettem'
datetime       '2023-03-15'
filepath       'C:\Users\user\Desktop\file.txt'
                
                Target : 'http://devhost:80/opt/dev/naukri/madhunettem/'
               
TextBook   : Reading
Classwork  : Writing, Reading
Homework   : Writing
RoughNotes : Writing 
GraphBook  : Writing, Reading
Blueprint  : Writing 
Guide      : Reading

txt***, json****,  csv***, excel***,  zip*, pdf*, xml*,
word  ppt image jpg  audio video

Operations:
-------------
1. Read data
2. Write data into file
3. Update content

file: empty file
    - C - append more content
    - R - read content 
    - U - update content
    - U - delete existing content and add from scratch
    - D - delete content



FILE HANDLING :
==================
Advantages of storing data in file:
------------------------------------
 - Data can be stored permanently
 - We can update the data in file whenever required
 - File can be shared to multiple users when required
 - To store huge amount of data, files are very helpful

 Types of files in python:
 -------------------------
 1. Text files   : Stores data in form of characters
 2. Binary files : Stores data in form of bytes
                   Can be used to store text,audio,video,images etc.,

To open a file :
----------------
                  open the file and read it 
        file_obj = open("filename", "open mode")
        
                #  open corepython.pdf in read mode 
                #  open introduction.doc in write mode 
                 

To close a file :
-----------------
        file_obj.close()


Mode      openmode                           Description :
------------------------------------------------------------------------------------------
w         Writes data into file.            If data exists already, it will be deleted and new data will be written
a         Appends data into file.           If data already exists it will start appending from last line of file
r         Reads data from file.             File pointer is positioned at beginning of file

w+        Writes and reads data of file     Previous data in the file will be deleted
r+        Reads and writes data into file   Previous data in the file will not be deleted
a+        Appends and reads data of file    File pointer will be at end of file
                                            If file does not exists,will create new file and writes data
x   Opens file in exclusive creation mode   If file already exists,file creation fails




'''


