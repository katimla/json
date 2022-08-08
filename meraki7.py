# Convert text file data to whatever file data may be, like given below?

# Text.txt:-  
# a= {"Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29"}

import json
a={}
filename="meraki7.file"
with open(filename) as f:
    for i in f:
        key,value=i.strip().split(None,1)
        a[key]=value
print(json.dumps(a,indent=4))
file=open("meraki7.json","w")
json.dump(a,file,indent=4)
file.close()

