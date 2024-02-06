# PROGRAM TO READ AND WRITE  DATA FROM A FILE

# Writing
out_data = open("C:/Users/nette/OneDrive/Desktop/names.txt", "w")
out_data.write("Welcome to the world of Python")
print("---After writing to file DATA : ", out_data)
out_data.close()

# Reading
obj = open("C:/Users/nette/OneDrive/Desktop/names.txt", "r")
in_data = obj.read()
print("---Reading from file--------  : ", in_data)
obj.close()
