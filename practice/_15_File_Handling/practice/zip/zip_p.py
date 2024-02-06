import zipfile

# print("----------zip started----------")
#
# zip_file = zipfile.ZipFile("files.zip", 'w')
# zip_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
# zip_file.close()
#
# print("----------zip closed----------")

# print("--------unzipping-------")
# unzip_file = zipfile.ZipFile("files.zip", 'r')
# # unzip_file.extractall('files1')
# unzip_file.extract('file1.txt')
# print("--------unzipping done-------")

unzip_files = zipfile.ZipFile("_02_ Variables_Notes.zip", 'r')
unzip_files.extractall('variables')
