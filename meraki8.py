
# import json
# a=[["neelam","programer","24","24000"],
# ["komal","trainer","24","20000"],
# ["anuradha","HR","25","40000"],
# ["Abhishek","manager","29","63000"]]
# b=["name","designation","age","salary"]
# d={}
# i=0
# while i<len(a):
#   s={}
#   m="emp"+str(i+1)
#   j=0
#   while j<len(a[i]):
#     s[b[j]]=a[i][j]
#     j=j+1
#   i=i+1
#   d[m]=s
# with open("meraki 8.json","w") as f:
#     y=json.dump(d,f,indent=1)
    

import json
a=["neelam","programer","24","24000"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
dic={}
dic1={}
dic2={}
dic3={}
dic4={}
i=0
while i<len(a):
  dic1[e[i]]=a[i]
  dic2[e[i]]=b[i]
  dic3[e[i]]=c[i]
  dic4[e[i]]=d[i]
  i=i+1
dic["emp1"]=dic1
dic["emp2"]=dic2
dic["emp3"]=dic3
dic["emp4"]=dic4
# print(dic)
with open("meraki 8.json","w") as f:
  y=json.dump(dic,f,indent=4)
f.close()

# f=open("meraki8.json","w")
# j=json.dump(dic,f,indent=4)
# f.close()


# Botshot is a SAAS company for hospitality. We are focusing to 
# enhance and upgrade our company system so that we could give the
# finest and formost importance and services to our clients. We are
# passionate to develop the world class integrated platform for
# hospitality to provide aceptional guest service. We look forward 
# to diccusing your specific requirment so that we can provide a
# meaningfull overview of our platform and how we can help you.
# Guest can be browse through contactless menus through different 
# channels and even raise a butler request. We are focusinng on
# Contactless checkin, menus  and Feedack management systems.
    

  

    