import csv
# reading a csv file
with open('phone_dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

# appending into csv file
"""
data = ['sai, nitesh, vizag, (891) 906-5372']
with open('phone_dataset.csv', 'a') as append_file:
    write = csv.writer(append_file)
    write.writerow(data)
"""