import json
# reading data
with open('dummy.json', 'r') as my_json_file:
    json_data = my_json_file.read()
    # pars the json data
    obj = json.loads(json_data)
    for index in range(len(obj)):
        # print(obj[index])
        print("name is", obj[index].get('name'))
        # print("mail is ", obj[index].get('email'),  end=" ")
        # print("address is", obj[index].get('address'))

