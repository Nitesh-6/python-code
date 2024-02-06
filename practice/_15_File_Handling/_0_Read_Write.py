""""""

# File Read Operation
'''
1. Open file
2. Perform Operation   Read/Write/Append/Update/Delete
3. Close the file
'''

# 1. Open File
file_obj = open('context.txt', 'r')  # "C:/Users/nettem/OneDrive/Desktop/context.txt"

# 2. Read File
data = file_obj.read()  # TextIOWrapper : read(self)
# print("----DATA ----- : ", data)

# 3. Close File
file_obj.close()



# File Write

# 1. Open File
file_obj = open('context10.txt', 'w')

# 2. Write Data
file_obj.write("Hello World Welcome to Python!!")

# 3. Close File
file_obj.close()

# import csv
#
# with open("_1_search_tele_results/phone_dataset.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
