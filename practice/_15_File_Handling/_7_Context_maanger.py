# https://www.geeksforgeeks.org/context-manager-in-python/
# Python program creating a
# context manager
''''''
'''

Context Manager in python :
-----------------------------
with  statement:
https://www.geeksforgeeks.org/context-manager-in-python/
http://book.pythontips.com/en/latest/context_managers.html
https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

Assignemnt :
Importance of Context Manager in python
How with statement internally works in python
Text file : Create Read Write Append Delete
            C      R    U     U        D
Excel file:
Zip file :

'''
class ContextManager:

    def __init__(self):                         # 2
        print('OBJECT --- init method called')

    def __enter__(self):                         # 3
        print('ENTER  --- Open Ops - enter()')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):   # 5
        print('EXIT  --- Close Ops - exit()')

print("---Before with-----")  # 1

with ContextManager() as f_obj:
    print('File ops 1')   # 4
    print('File ops 2')
    print('File ops 3')

print("---After with-----")  # 6

'''
---Before with-----
OBJECT --- init method called
ENTER  --- enter method called : open file 
with line 1
with line 2
with line 3
EXIT  --- exit method called   : close file 
---After with-----

'''




class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        print("File Manager : __init__")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("File Manager : __enter__")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        print("File Manager : __exit__")

    # loading a file


with FileManager('context.txt', 'w') as f_obj:
    print("I am in CM : Before")
    f_obj.write('---Data written using manual context manager----')
    print("I am in CM : After")
    print("Is file closed1 ? ", f_obj.closed)

print("Is file closed2 ? ", f_obj.closed)


'''
txt* files
csv* files
excel* files
zip* files 
pdf files
images
audio files
video files
'''