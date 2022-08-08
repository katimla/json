# import json

# x={1:"Katimla",2:24,"city":"Imphal"}
# y=json.dumps(x)
# print(y)

#loads

# import json
# x='{"name":"Katimla","age":24,"city":"Imphal"}'
# y=json.loads(x)
# print(y)

# import json
# x = '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])


# import json
# a="""{"a":1,"b":2,"c":3}"""
# x=json.loads(a)
# print(x)

# import json

# dic={'name':'Katimla','age':21,'class':1}
# a=json.dumps(dic)
# with open("file.json","w") as dict:
#     json.dump(dic,dict,indent=2)

# dic={1:"Katimla","age":21,"class":1}
# # a=json.loads(dic)
# with open("store.json","w") as dict:
#     x=json.dumps(dic)
# print(x)



# import json   
# dictionary = json.load(open("in.json","r"))
# print(dictionary)


# PrettyPrint following JSON data with indent level 2 and key-value 
# separators should be (",", " = ").


import json
d= {"key1": "value1", "key2": "value2"}
print(json.dumps(d,indent=2,separators=(",","=")))